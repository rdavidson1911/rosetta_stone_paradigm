# Setting Up Email Notifications for GitHub Repository Activities

This guide will help you set up email notifications for new commits and pull requests on your GitHub repository.

## 1. GitHub Notification Settings

1. Log in to your GitHub account.
2. Click on your profile picture in the top-right corner and select "Settings".
3. In the left sidebar, click on "Notifications".
4. Under the "Email notification preferences" section:
   - Ensure your email address is correct.
   - Check the box for "Email" next to "Pull requests" and "Pushes".
5. Scroll down and click "Save changes".

## 2. Repository-Specific Settings

1. Go to your repository page.
2. Click on "Settings" in the top menu.
3. In the left sidebar, click on "Notifications".
4. Ensure that "Watching" is selected. This will notify you of all conversations and activities in this repository.

## 3. Setting Up a Webhook for More Detailed Notifications

For more customized notifications, you can set up a webhook that sends data to a service that then emails you.

1. Go to your repository page.
2. Click on "Settings" in the top menu.
3. In the left sidebar, click on "Webhooks".
4. Click on "Add webhook".
5. For the Payload URL, you'll need a service that can receive webhook data and send emails. Services like Zapier or IFTTT can do this.
6. Set the Content type to "application/json".
7. For "Which events would you like to trigger this webhook?", select "Let me select individual events".
8. Check the boxes for "Pull requests" and "Pushes".
9. Click "Add webhook" at the bottom of the page.

## 4. Using a Third-Party Service (e.g., Zapier)

1. Sign up for a Zapier account (or similar service).
2. Create a new Zap.
3. Choose GitHub as the trigger app.
4. Select "New Push" or "New Pull Request" as the trigger event.
5. Connect your GitHub account and select your repository.
6. For the action, choose "Email" or your preferred email service.
7. Set up the email details, using the data from the GitHub trigger to customize your email content.
8. Test and turn on your Zap.

## 5. Testing Your Setup

1. Make a small commit to your repository or create a test pull request.
2. Check your email to see if you receive a notification.
3. If using a webhook, check the webhook's recent deliveries in GitHub to ensure it's working correctly.

Remember to adjust your notification settings if you start receiving too many emails. You can always fine-tune which activities trigger notifications.

For more detailed information, refer to [GitHub's documentation on managing notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/setting-up-notifications).
