# Security Configuration Guide

## GitHub Secrets Setup

### Required Secrets:
1. **PROD_DB_PASSWORD** - Production database password
2. **PROD_API_KEY** - Production API key for external services
3. **SLACK_WEBHOOK** - Slack webhook URL for notifications

### Setting up secrets:
1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add each secret with its value

## Environment Variables

### Non-sensitive (.env file):
- ENVIRONMENT
- APP_VERSION
- PORT
- LOG_LEVEL
- DB_HOST
- DB_PORT

### Sensitive (GitHub Secrets):
- Database passwords
- API keys
- Webhook URLs
- Private keys

## Security Checklist

- [ ] No hardcoded passwords in code
- [ ] All sensitive data in GitHub Secrets
- [ ] .env files in .gitignore
- [ ] Regular security scans enabled
- [ ] Manual approval for production
- [ ] Audit logs enabled