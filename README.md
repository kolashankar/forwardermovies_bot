Telegram Auto Forwarder Bot - Comprehensive Guide

Table of Contents:
1. Introduction
2. Installation and Setup
3. Configuration
4. Basic Usage
5. Commands
6. Features
   6.1. Automatic Forwarding
   6.2. Media Forwarding
   6.3. Shortlink Integration
   6.4. Watermarking
   6.5. Content Filtering
   6.6. Scheduled Forwarding
   6.7. Multi-language Support
   6.8. User Management
   6.9. Auto-backup System
   6.10. Analytics Integration
7. Premium Features
8. Advanced Configuration
9. Deployment
10. Troubleshooting
11. Frequently Asked Questions (FAQ)
12. Contributing
13. License and Disclaimer

1. Introduction
----------------
The Telegram Auto Forwarder Bot is a powerful tool designed to automatically forward messages from specified source channels to designated destination channels on Telegram. This bot offers a wide range of features and premium options, providing unparalleled flexibility and advanced functionality for managing content across Telegram channels.

2. Installation and Setup
--------------------------
To install and set up the Telegram Auto Forwarder Bot, follow these steps:

a. Clone the repository:
   git clone https://github.com/yourusername/telegram-auto-forwarder-bot.git
   cd telegram-auto-forwarder-bot

b. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

c. Install the required packages:
   pip install -r requirements.txt

d. Create a `.env` file in the project root and add your configuration (see Configuration section).

e. Initialize the database:
   python init_db.py

f. Start the bot:
   python main.py

3. Configuration
-----------------
Create a `.env` file in the project root directory with the following variables:

BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_USERNAME=your_bot_username
DATABASE_URL=your_mongodb_url_here
REDIS_URL=your_redis_url_here
SOURCE_CHANNELS=channel1,channel2
DESTINATION_CHANNELS=channel3,channel4
ADMIN_USER_IDS=123456789,987654321
OWNER_ID=your_telegram_id
LOG_CHANNEL_ID=log_channel_id
ERROR_LOG_CHANNEL_ID=error_log_channel_id
PREMIUM_CHANNEL_ID=premium_channel_id
BACKUP_CHANNEL_ID=backup_channel_id
DEFAULT_LANGUAGE=en
SUPPORTED_LANGUAGES=en,es,fr,de,it
MAX_USERS=1000
USER_EXPIRY_DAYS=30
USER_COOLDOWN=60
RATE_LIMIT=100
MAX_CONCURRENT_TASKS=5
ENABLE_AUTO_BACKUP=True
BACKUP_INTERVAL=86400
ENABLE_ANALYTICS=True
ANALYTICS_TOKEN=your_analytics_token
ANALYTICS_PLATFORM=your_analytics_platform
SHORTLINK_API=your_shortlink_api_key
SHORTLINK_URL=your_shortlink_api_url
WATERMARK_TEXT=Your Watermark
WATERMARK_POSITION=bottom-right
BANNED_WORDS=word1,word2,word3
ALLOWED_CONTENT_TYPES=text,photo,video,document
FORWARD_MEDIA=True
SCHEDULER_ENABLED=True

4. Basic Usage
---------------
To start using the Telegram Auto Forwarder Bot:

1. Ensure all configuration is set up correctly.
2. Run the bot: `python main.py`
3. Open your Telegram client and start a chat with your bot.
4. Use the `/start` command to initialize the bot and get a list of available commands.

5. Commands
------------
Here's a list of available commands and their usage:

Basic Commands:
- /start - Initialize the bot and get a welcome message
- /help - Display available commands and their usage
- /status - Check the current status of the bot
- /settings - View and modify bot settings

Channel Management:
- /add_source <channel_id> - Add a new source channel
- /add_destination <channel_id> - Add a new destination channel
- /list_channels - List all configured channels
- /remove_channel <channel_id> - Remove a channel from the configuration

Forwarding Control:
- /start_forwarding - Start the forwarding process
- /stop_forwarding - Stop the forwarding process
- /set_delay <seconds> - Set the delay between forwards

Content Management:
- /set_filter <filter_type> <value> - Set content filters
- /add_banned_word <word> - Add a word to the banned list
- /remove_banned_word <word> - Remove a word from the banned list
- /set_caption <caption_template> - Set a custom caption template

Premium Commands:
- /upgrade - Upgrade to premium
- /set_watermark <text> [position] - Set watermark text and options
- /schedule <cron_expression> <action> - Set up scheduled forwarding
- /analytics - View detailed analytics (premium only)
- /custom_command <command_name> <action> - Create a custom command (premium only)

Admin Commands:
- /broadcast <message> - Send a message to all users
- /ban_user <user_id> - Ban a user from using the bot
- /unban_user <user_id> - Unban a user
- /list_users - List all bot users
- /set_user_expiry <user_id> <days> - Set expiry for a user's account
- /reset_user_cooldown <user_id> - Reset cooldown for a user

System Commands:
- /backup - Manually trigger a backup
- /restore <backup_id> - Restore from a backup
- /logs - View recent logs
- /update - Check for and apply bot updates (admin only)

6. Features
------------

6.1. Automatic Forwarding
--------------------------
The bot monitors specified source channels and forwards new messages to destination channels based on your configuration.

To set up:
1. Use `/add_source <channel_id>` to add source channels.
2. Use `/add_destination <channel_id>` to add destination channels.
3. Use `/start_forwarding` to begin the forwarding process.

Customize with:
- `/set_delay <seconds>` to add a delay between forwards.
- `/set_filter <filter_type> <value>` to apply content filters.

Example:
/add_source -1001234567890
/add_destination -1009876543210
/set_delay 5
/set_filter content_type photo,video
/start_forwarding

This setup will forward only photos and videos from the source channel to the destination channel with a 5-second delay between each forward.

6.2. Media Forwarding
----------------------
The bot can forward various types of media, including photos, videos, documents, and audio files.

To configure:
1. Set `FORWARD_MEDIA=True` in your `.env` file.
2. Use `/set_filter content_type <types>` to specify allowed media types.

Example:
/set_filter content_type photo,video,document

This will allow the bot to forward photos, videos, and documents, while ignoring other types of content.

6.3. Shortlink Integration
---------------------------
Automatically convert links in forwarded messages to short URLs using a configured shortlink service.

To set up:
1. Add your shortlink API details to the `.env` file:
   SHORTLINK_API=your_api_key
   SHORTLINK_URL=your_api_url
2. Enable shortlink conversion in your settings:
   /settings shortlink_enabled true

The bot will now automatically convert links in forwarded messages. You can customize the shortlink behavior with additional settings:
- `/settings shortlink_domains domain1,domain2` to specify which domains should be converted
- `/settings shortlink_position start` to place the shortened link at the start of the message (options: start, end)

6.4. Watermarking
------------------
Add custom watermarks to forwarded media (Premium feature).

To use:
1. Use `/set_watermark <text> [position]` to configure watermark text and options.
   Example: `/set_watermark "My Channel" bottom-right`
2. Enable watermarking in your settings:
   /settings watermark_enabled true

Additional watermark customization:
- `/settings watermark_opacity 0.7` to set the opacity (0.0 to 1.0)
- `/settings watermark_font Arial` to set the font
- `/settings watermark_color white` to set the color

The bot will now automatically apply the watermark to forwarded media.

6.5. Content Filtering
-----------------------
Set up word filters and content type restrictions to control what gets forwarded.

To configure:
1. Use `/add_banned_word <word>` to add words to the filter.
   Example: `/add_banned_word spam`
2. Use `/set_filter content_type <types>` to set up content type restrictions.
   Example: `/set_filter content_type text,photo`
3. Adjust `BANNED_WORDS` and `ALLOWED_CONTENT_TYPES` in your `.env` file for more control.

Advanced filtering (Premium):
- Use regex patterns: `/set_filter regex \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
- Set up complex conditions: `/set_filter condition "len(message.text) > 100 and 'important' in message.text.lower()"`

6.6. Scheduled Forwarding
--------------------------
Set up automated forwarding schedules to control when messages are forwarded.

To use:
1. Enable scheduling in your `.env` file: `SCHEDULER_ENABLED=True`
2. Use the `/schedule <cron_expression> <action>` command to set up forwarding schedules.

Example:
/schedule "0 9 * * *" start_forwarding
/schedule "0 17 * * *" stop_forwarding

This setup will start forwarding at 9 AM and stop at 5 PM every day.

Advanced scheduling (Premium):
- Set up multiple schedules for different channels or content types
- Use more complex cron expressions for fine-grained control

6.7. Multi-language Support
----------------------------
The bot supports multiple languages for user interactions, making it accessible to a global audience.

To configure:
1. Set `DEFAULT_LANGUAGE` in your `.env` file.
2. Add supported languages to `SUPPORTED_LANGUAGES` in your `.env` file.
3. Users can change their language preference using:
   /settings language <lang_code>

Example: `/settings language es` to switch to Spanish.

To add a new language:
1. Create a new language file in the `locales` directory (e.g., `fr.json` for French).
2. Translate all strings in the file.
3. Add the language code to `SUPPORTED_LANGUAGES` in your `.env` file.

6.8. User Management
---------------------
Manage bot users, including expiration, cooldowns, and limits.

Admin commands:
- `/list_users` to view all users.
- `/ban_user <user_id>` to ban a user.
- `/unban_user <user_id>` to unban a user.
- `/set_user_expiry <user_id> <days>` to set an expiration for a user's account.
- `/reset_user_cooldown <user_id>` to reset the cooldown period for a user.

Configure in `.env`:
- `MAX_USERS`: Maximum number of users allowed.
- `USER_EXPIRY_DAYS`: Number of days before user accounts expire.
- `USER_COOLDOWN`: Cooldown period between user actions.

Example user management workflow:
1. List all users: `/list_users`
2. Ban a user: `/ban_user 123456789`
3. Set user expiry: `/set_user_expiry 123456789 30`
4. Reset user cooldown: `/reset_user_cooldown 123456789`

User management best practices:
- Regularly review the user list to identify inactive accounts
- Set appropriate expiration periods to manage user turnover
- Use cooldowns to prevent abuse of bot features
- Communicate clearly with users about account status and expiration

6.9. Auto-backup System
------------------------
Automatically backup bot data and configurations to ensure data safety and easy recovery.

To enable:
1. Set `ENABLE_AUTO_BACKUP=True` in your `.env` file.
2. Configure `BACKUP_INTERVAL` (in seconds) and `BACKUP_CHANNEL_ID` in `.env`.
3. The bot will automatically create backups at the specified interval.

Manual backup and restore:
- Use `/backup` to manually trigger a backup.
- Use `/restore <backup_id>` to restore from a specific backup.

Backup contents:
- User data
- Channel configurations
- Bot settings
- Forwarding rules and filters

Best practices:
- Keep multiple backups (the bot stores the last 5 by default)
- Regularly test the restore process
- Store backups in a secure, separate location

6.10. Analytics Integration
----------------------------
Track bot usage and performance metrics for insights into your forwarding operations.

To set up (Premium feature):
1. Set `ENABLE_ANALYTICS=True` in your `.env` file.
2. Configure `ANALYTICS_TOKEN` and `ANALYTICS_PLATFORM` in `.env`.
3. Use the `/analytics` command to view reports.

Available analytics:
- Message volume (daily, weekly, monthly)
- Peak forwarding times
- Most active source and destination channels
- Content type distribution
- User engagement metrics
- Error rates and types

Example analytics command:
/analytics weekly

This will display a report of the past week's forwarding activity, including message volume, peak times, and top channels.

7. Premium Features
--------------------
Premium features can be activated by upgrading your account. To upgrade, use the `/upgrade` command and follow the instructions. Premium features include:

1. Increased Forwarding Limits: Forward up to 10,000 messages per day (compared to 1,000 for free users).
2. Additional Channels: Add up to 50 source and 50 destination channels (compared to 10 each for free users).
3. Advanced Filtering: Use regex and more complex filtering options for precise content control.
4. Priority Support: Get faster responses to your queries through a dedicated support channel.
5. Custom Branding: Add your own branding to forwarded messages, including custom watermarks and link shorteners.
6. Enhanced Analytics: Access detailed statistics and performance metrics, including engagement rates and peak activity times.
7. Exclusive Commands: Access to premium-only commands for advanced bot management.
8. Early Feature Access: Be the first to try new features before they're released to all users.

To activate premium features after upgrading:
1. Use `/status` to verify your premium status.
2. Use specific premium commands like `/set_watermark` or `/analytics`.
3. Adjust your configuration to take advantage of higher limits and additional features.

8. Advanced Configuration
--------------------------
Fine-tune your bot's behavior with advanced configuration options:

1. Custom Filters:
   Create complex filtering rules using Python expressions.
   Example in `config.py`:
   ```python
   CUSTOM_FILTERS = [
       lambda message: len(message.text) > 100 and '#important' in message.text,
       lambda message: message.forward_from_chat.id in VERIFIED_SOURCES
   ]
