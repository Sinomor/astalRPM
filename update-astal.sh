#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

DEFAULT_UPSTREAM="https://github.com/Aylur/astal.git"

declare -A UPSTREAM_REPOS=(
    ["libastal-niri"]="https://github.com/sameoldlab/niri-gtk.git"
)

UPSTREAM_BRANCH="main"

get_upstream_commit() {
    local repo="$1"

    git ls-remote "$repo" "refs/heads/$UPSTREAM_BRANCH" |
        awk '{print $1}'
}

declare -A COMMITS

echo "Fetching upstream commits..."
echo

# Get commits for all unique upstream repositories.
for repo in "$DEFAULT_UPSTREAM" "${UPSTREAM_REPOS[@]}"; do
    [[ -n "${COMMITS[$repo]+x}" ]] && continue

    echo "Fetching $repo..."

    commit="$(get_upstream_commit "$repo")"

    if [[ -z "$commit" ]]; then
        echo "ERROR: failed to get commit from $repo" >&2
        exit 1
    fi

    COMMITS["$repo"]="$commit"

    echo "$commit"
done

snapshot_date="$(date -u +%Y%m%d)"

echo
echo "Snapshot date: $snapshot_date"
echo

updated=0
skipped=0

while IFS= read -r -d '' spec; do
    package_dir="$(basename "$(dirname "$spec")")"

    # Packages using a different upstream.
    if [[ -n "${UPSTREAM_REPOS[$package_dir]+x}" ]]; then
        repo="${UPSTREAM_REPOS[$package_dir]}"

    # libastal-* and quarrel are part of Aylur/astal.
    elif [[ "$package_dir" == libastal-* || "$package_dir" == "quarrel" ]]; then
        repo="$DEFAULT_UPSTREAM"

    # Everything else in the repository is unrelated.
    else
        echo "Skipping $spec (not an Astal package)"
        ((skipped++)) || true
        continue
    fi

    # Meta packages don't have their own upstream snapshot.
    if ! grep -q '^%global commit ' "$spec"; then
        echo "Skipping $spec (no upstream commit)"
        ((skipped++)) || true
        continue
    fi

    if ! grep -q '^%global date ' "$spec"; then
        echo "ERROR: $spec contains '%global commit' but no '%global date'" >&2
        exit 1
    fi

    commit="${COMMITS[$repo]}"

    echo "Updating $spec"
    echo "  upstream: $repo"
    echo "  commit:   $commit"

    sed -i \
        -E "s/^%global commit .*/%global commit $commit/" \
        "$spec"

    sed -i \
        -E "s/^%global date .*/%global date $snapshot_date/" \
        "$spec"

    ((updated++)) || true
    echo
done < <(
    find "$SCRIPT_DIR/specs" \
        -type f \
        -name '*.spec' \
        -print0 |
    sort -z
)

echo "Updated: $updated"
echo "Skipped: $skipped"
echo

if git diff --quiet -- specs; then
    echo "No changes."
else
    echo "Changes:"
    git diff -- specs
fi
