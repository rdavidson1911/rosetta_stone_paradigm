# Git Command Reference

This document provides a quick reference for common Git commands used in our project.

## Basic Git Commands

- Initialize a new Git repository:
  ```
  git init
  ```

- Clone a repository:
  ```
  git clone <repository-url>
  ```

- Check the status of your repository:
  ```
  git status
  ```

- Add files to the staging area:
  ```
  git add <file-name>
  git add .  # Add all changes
  ```

- Commit changes:
  ```
  git commit -m "Your commit message"
  ```

- Push changes to a remote repository:
  ```
  git push <remote-name> <branch-name>
  ```

- Pull changes from a remote repository:
  ```
  git pull <remote-name> <branch-name>
  ```

## Working with Remotes

- List remote repositories:
  ```
  git remote -v
  ```

- Add a new remote:
  ```
  git remote add <remote-name> <repository-url>
  ```

- Change the URL of an existing remote repository:
  ```
  git remote set-url <remote-name> <new-url>
  ```

- Remove a remote:
  ```
  git remote remove <remote-name>
  ```

## Branching

- Create a new branch:
  ```
  git branch <branch-name>
  ```

- Switch to a branch:
  ```
  git checkout <branch-name>
  ```

- Create and switch to a new branch:
  ```
  git checkout -b <branch-name>
  ```

- Merge a branch into the current branch:
  ```
  git merge <branch-name>
  ```

- Delete a branch:
  ```
  git branch -d <branch-name>
  ```

## Other Useful Commands

- View commit history:
  ```
  git log
  ```

- Discard changes in working directory:
  ```
  git checkout -- <file-name>
  ```

- Create a tag:
  ```
  git tag <tag-name>
  ```

## Appendix: SSH vs HTTPS Connections

Git supports two primary protocols for secure communication with remote repositories: SSH and HTTPS. Here's a comparison of the two:

### SSH (Secure Shell)

- **Pros:**
  - More secure
  - Can use SSH keys for authentication (no need to enter password each time)
  - Faster for frequent transactions
- **Cons:**
  - Requires SSH key setup
  - May be blocked by some firewalls

### HTTPS (Hypertext Transfer Protocol Secure)

- **Pros:**
  - Easier to set up initially
  - Works through most firewalls
  - Can use credential helpers for password caching
- **Cons:**
  - May require entering username/password more frequently
  - Slightly slower than SSH for frequent transactions

### Changing between SSH and HTTPS

To change the URL of a remote repository (e.g., from HTTPS to SSH or vice versa), use the following command:

```
git remote set-url <remote-name> <new-url>
```

For example, to change the 'origin' remote to use HTTPS for the Rosetta Stone Paradigm project:

```
git remote set-url origin https://github.com/rdavidson1911/rosetta_stone_paradigm.git
```

To change to SSH (assuming you have SSH set up with GitHub):

```
git remote set-url origin git@github.com:rdavidson1911/rosetta_stone_paradigm.git
```

### Official GitHub Documentation

For more detailed information, refer to these official GitHub guides:

- [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) (for HTTPS authentication)
- [Switching remote URLs from HTTPS to SSH](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories#switching-remote-urls-from-https-to-ssh)

Remember to replace `<placeholder>` with actual values when using these commands.

For more detailed information on Git commands, consult the [official Git documentation](https://git-scm.com/doc).

## Setting Up SSH for GitHub

SSH provides a secure way to connect to GitHub without needing to enter your username and password each time. Here's how to set it up:

1. Generate a new SSH key:
   ```
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   When prompted, you can press Enter to accept the default file location, or specify a custom name (e.g., `rosetta`).

2. Start the ssh-agent in the background:
   ```
   eval "$(ssh-agent -s)"
   ```

3. Add your SSH private key to the ssh-agent:
   ```
   ssh-add ~/.ssh/id_rsa  # or the path to your key if you used a custom name
   ```

4. Copy the contents of your public key:
   ```
   cat ~/.ssh/id_rsa.pub  # or your_custom_name.pub
   ```

5. Add the SSH key to your GitHub account:
   - Go to GitHub and sign in
   - Click on your profile photo in the top right corner
   - Select "Settings" from the dropdown menu
   - In the left sidebar, click on "SSH and GPG keys"
   - Click the "New SSH key" button
   - Give your key a descriptive title
   - Paste your public key into the "Key" field
   - Click "Add SSH key"

6. Test your SSH connection:
   ```
   ssh -T git@github.com
   ```
   If successful, you'll see a message like: "Hi username! You've successfully authenticated, but GitHub does not provide shell access."

7. Update your remote repository URL to use SSH:
   ```
   git remote set-url origin git@github.com:username/repository.git
   ```
   Replace 'username' and 'repository' with your GitHub username and repository name.

Now you can push and pull from your GitHub repository using SSH authentication.

## Advanced GitHub Features

### GitHub Actions
To set up a basic CI workflow:
1. Create a `.github/workflows/ci.yml` file in your repository
2. Add the following content:
   ```yaml
   name: CI
   on: [push, pull_request]
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Run tests
         run: |
           # Add your test commands here
   ```

### GitHub Projects
To create a new project board:
1. Go to the 'Projects' tab in your repository
2. Click 'New project'
3. Choose a template or start from scratch
4. Add columns like 'To do', 'In progress', 'Done'

### GitHub Insights
To view repository insights:
1. Go to the 'Insights' tab in your repository
2. Explore different sections like 'Contributors', 'Traffic', 'Commits'

### GitHub Pages
To set up GitHub Pages:
1. Go to repository settings
2. Scroll down to the 'GitHub Pages' section
3. Choose a source branch for your site
4. Your site will be available at `https://<username>.github.io/<repository>`

For more detailed information on these features, refer to the [GitHub Docs](https://docs.github.com/en).

## GitHub Webhooks

Webhooks allow external services to be notified when certain events happen in your repository. Unlike polling, where a service constantly checks for updates, webhooks push notifications when events occur, making them more efficient.

### Setting Up a Webhook

1. Go to your repository on GitHub.
2. Click on "Settings" in the repository menu.
3. Select "Webhooks" from the left sidebar.
4. Click on "Add webhook".
5. In the "Payload URL" field, enter the URL of the external service that will receive the webhook payload.
6. Choose the content type (usually `application/json`).
7. Select which events should trigger the webhook.
8. Click "Add webhook" to save.

### Common Use Cases for Webhooks

- Trigger CI/CD pipelines on push or pull request events.
- Update an external issue tracker when issues are created or modified in GitHub.
- Notify a chat service (like Slack) of new commits or pull requests.
- Trigger automatic deployment when changes are pushed to a specific branch.

### Securing Webhooks

- Use HTTPS for the Payload URL to encrypt data in transit.
- Set a secret token to validate that the webhook came from GitHub.
- Implement IP whitelisting if your server allows it.

### Testing Webhooks

GitHub provides a "Recent Deliveries" section where you can see the payload and response for each webhook event. You can also trigger a test payload from this interface.

### Webhook Payload Example

Here's a simplified example of what a webhook payload might look like for a push event:

```
## Using Git Large File Storage (LFS)

Git LFS is used for versioning large files, keeping them out of Git's main repository while still tracking them.

### Setting up Git LFS

1. Install Git LFS:
   ```
   sudo apt-get install git-lfs  # On Ubuntu/Debian
   ```

2. Initialize Git LFS:
   ```
   git lfs install
   ```

3. Track large files:
   ```
   git lfs track "*.pcapng"
   ```

4. Ensure .gitattributes is tracked:
   ```
   git add .gitattributes
   ```

### Using Git LFS

- Add and commit files as normal:
  ```
  git add large_file.pcapng
  git commit -m "Add large file"
  ```

- Push to GitHub:
  ```
  git push origin main
  ```

### Pulling a repository with LFS files

- Clone as normal:
  ```
  git clone https://github.com/username/repo.git
  ```

- LFS files will be downloaded automatically.

### Checking LFS status

- List tracked patterns:
  ```
  git lfs track
  ```

- List LFS files in your repository:
  ```
  git lfs ls-files
  ```

For more information, visit the [Git LFS website](https://git-lfs.github.com/).
