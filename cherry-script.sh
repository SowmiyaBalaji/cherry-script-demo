read -p "Enter the target branch:" target_branch

git checkout "$target_branch"

commit_hash_array=()
read -p "Enter the commit hashes:" -r hash_inputs
read -r -a commit_hash_array <<< "$hash_inputs"

for commit_hash in "${commit_hash_array[@]}"
do
	git cherry-pick "$commit_hash"
if [$? != 0] 
then
	echo "Cherry pick of commit hash $commit_hash has conflicts. Resolve it manually"
	exit 1
fi
done

git push origin "$target_branch"
if [$? != 0]
then
        echo "Git push failed"
        exit 1
fi

echo "Cherry pick done successfully"
