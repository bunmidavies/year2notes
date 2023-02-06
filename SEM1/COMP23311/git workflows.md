[[COMP23311]] `week 7`

*Git workflows are patterns of collaborative usage of Git that work well for particular team configurations and project requirements*

Git workflows specify things such as:
- Repository setup/initialisation: cluster of clones, cluster of forks, dictators & lieutenants (similar to cluster of forks)
- Branching strategies
- Code integration strategies
- File management
- Syncing
- Tagging, branch naming, version bumping

COMP23311 covers 5 git workflows, all based on the idea of  ==lines of development==

A ==line of development== is a contiguous sequence of code versions that have a ==common role== in the development process

### <span style="background-color:#797ca3;padding:3px;border-radius:5px;">Feature Branches</span>

- The workflow used in the team courseworks, also known as a ==foundational== workflow
- There are typically 2-3 lines of development:
	- main - the branch which always stays
	- change/fix - the 'features' themselves - short lived branches
	- release - ==tags== on main / short lived branches for release prep
- changes/fixes are integrated into main using ==merges==
- ==rebasing== is used for syncing local with remote

### <span style="background-color:#262963;padding:3px;border-radius:5px;">Feature Branches + Code Review</span>

- The same basic workflow as feature branches
- The difference is that ==integration== is done through pull/merge ==requests==
- Code review can cause extra commits to fix any comments made, but other than this the commit graph will look the same

### <span style="background-color:#b37b4b;padding:3px;border-radius:5px;">GitFlow</span>

- The first workflow to become generally known and used

GitFlow has two main lines of development - ==main==, and ==integration==. There are feature branches which branch ==off integration==, and merge back into Integration (using a ==non fastforward merge==)

GitFlow also has ==hotfixes==, short lived branches which allow you to branch off main and merge back into main ==and== integration

- There is more room for error within GitFlow in comparison to other workflows
- Gives ==several levels of protection== for team development and released code
- However, many people believe it is ==unnecessarily complex==

### <span style="background-color:#615041;padding:3px;border-radius:5px;">GitHub Flow</span>

- A simpler version of GitFlow, with emphasis on ==clean builds and code quality==
- The workflow also assumes a ==cluster of forks== repo configuration
- One long lived branch for integration and main
- Short lived branches for changes, fixes and releases which branch off main and integrate to main
- The difference between GitHub Flow and feature branches is that ==every commit on main is deployable== with GitHub Flow
- Code review is done through pull requests (GitHubs version of Merge Requests), and must be tested in product before merging

### <span style="background-color:#734d62;padding:3px;border-radius:5px;">Trunk-Based Development</span>

- The aim of trunk-based development is to ==keep a clean development history== - trunk supports continuous deployment and delivery
- The ==trunk== is a long lived branch for everything
- Change/fix/release work is done on a ==local master==
- Integration is done by ==squash and rebasing==
- Trunk only ever contains ==clean and deployable code==