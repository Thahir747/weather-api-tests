#!/attr/bin/env bash

# Stop execution if any command fails
set -e

echo "========================================="
echo "🚀 Starting Git Sync Process..."
echo "========================================="

# 1. Check if remote origin is configured
if ! git remote | grep -q "origin"; then
    echo "🔗 Connecting to GitHub..."
    git remote add origin https://github.com/Thahir747/weather-api-tests.git
else
    echo "✅ Remote origin connection found."
fi

# 2. Stage and package changes
echo "📦 Staging project updates..."
git add .

# Check if there are actually changes to commit
if git diff-index --quiet HEAD --; then
    echo "ℹ️  No new changes found to commit."
else
    echo "💾 Committing files..."
    git commit -m "docs: upgrade README with professional structure and badges"
fi

# 3. Synchronize with GitHub remote history safely
echo "🔄 Syncing remote repository history..."
git pull origin master --allow-unrelated-histories --no-rebase || true

# 4. Push updates upstream
echo "📤 Uploading framework to GitHub..."
git push origin master

echo "========================================="
echo "🎉 Success! Refresh your GitHub repository page."
echo "========================================="