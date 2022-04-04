from git import Repo

new_repo = Repo.init(r"C:\Users\unnimaya_pp\test\git")


#Repo.clone_from('https://github.com/MAYAGIT07/test.git', r"C:\Users\unnimaya_pp\test\git")
from git import Repo

repo = Repo(r"C:\Users\unnimaya_pp\test\git")

# List all branches
for branch in repo.branches:
    print(branch)

# Create a new branch
repo.git.branch('my_new_branch')

# To checkout to a branch:
repo.git.checkout('branch_name')

repo.git(test)
