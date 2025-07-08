# 🔧 GitHub MCP Setup Guide

## ✅ Installation Complete

The GitHub MCP server has been successfully installed and configured for Claude Code!

## 📋 What's Been Done

1. **✅ Installed GitHub MCP Server** (`@modelcontextprotocol/server-github`)
2. **✅ Added MCP Configuration** to Claude Code settings
3. **✅ Set up Environment Variables** for GitHub token

## 🔑 Next Step: Set Up GitHub Token

You need to create a GitHub Personal Access Token for the MCP server to work.

### Step 1: Create GitHub Personal Access Token

1. **Go to GitHub.com** and log in
2. **Click your profile picture** → **Settings**
3. **Scroll down** to **Developer settings** (bottom of left sidebar)
4. **Click "Personal access tokens"** → **"Tokens (classic)"**
5. **Click "Generate new token"** → **"Generate new token (classic)"**
6. **Fill out the form:**
   - **Note**: "Claude Code MCP Server"
   - **Expiration**: "90 days" (or your preference)
   - **Select scopes** (check these boxes):
     - ✅ `repo` (Full control of private repositories)
     - ✅ `read:user` (Read all user profile data)
     - ✅ `user:email` (Access user email addresses)
     - ✅ `read:org` (Read organization membership)
     - ✅ `workflow` (Update GitHub Action workflows)

7. **Click "Generate token"**
8. **Copy the token immediately** (you won't be able to see it again!)

### Step 2: Set Environment Variable

Choose one of these methods to set your GitHub token:

#### Option A: Add to Shell Profile (Recommended)

1. **Open Terminal**
2. **Edit your shell profile**:
   ```bash
   nano ~/.zshrc
   ```
   (or `~/.bashrc` if using bash)

3. **Add this line at the end**:
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```

4. **Save and exit** (Ctrl+X, then Y, then Enter)
5. **Reload your shell**:
   ```bash
   source ~/.zshrc
   ```

#### Option B: Set for Current Session Only

```bash
export GITHUB_TOKEN="your_token_here"
```

### Step 3: Verify Installation

1. **Restart Claude Code** (if it's running)
2. **Check if MCP is working**:
   ```bash
   npx @modelcontextprotocol/server-github --help
   ```

## 🎯 GitHub MCP Capabilities

Once set up, you'll have access to these GitHub features through Claude Code:

### **Repository Management**
- Create, clone, and manage repositories
- Browse repository contents
- View commit history and branches

### **Issues & Pull Requests**
- Create, update, and close issues
- Manage pull requests
- Add comments and reviews

### **Code Operations**
- Search code across repositories
- View file contents
- Compare branches and commits

### **Automation**
- Trigger GitHub Actions workflows
- Manage repository settings
- Handle webhooks and integrations

## 🔧 Configuration Details

The MCP server has been configured in your Claude Code settings:

**Location**: `~/.claude/settings.json`

**Configuration**:
```json
{
  "model": "sonnet",
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. **Token Not Found**
- Make sure you've set the `GITHUB_TOKEN` environment variable
- Restart your terminal/Claude Code after setting the token
- Verify the token is set: `echo $GITHUB_TOKEN`

#### 2. **Permission Denied**
- Check your token scopes (see Step 1 above)
- Make sure the token hasn't expired
- Try regenerating the token with proper scopes

#### 3. **MCP Server Not Starting**
- Verify installation: `npm list -g @modelcontextprotocol/server-github`
- Check Node.js version: `node --version` (should be 18+)
- Restart Claude Code completely

#### 4. **Invalid Token**
- Token might be expired or revoked
- Generate a new token following Step 1
- Update the environment variable

### Test the Setup

After setting up the token, test the connection:

```bash
# Test if token is set
echo $GITHUB_TOKEN

# Test MCP server
npx @modelcontextprotocol/server-github --help
```

## 🚀 Usage Examples

Once set up, you can use GitHub MCP features in Claude Code:

- **"Show me my GitHub repositories"**
- **"Create a new issue in my project"**
- **"What are the latest commits in my main branch?"**
- **"Help me create a pull request"**
- **"Search for code containing 'authentication' in my repos"**

## 🔒 Security Notes

- **Keep your token secure** - never share it or commit it to repositories
- **Use minimal scopes** - only grant permissions you need
- **Set reasonable expiration** - tokens should expire periodically
- **Revoke unused tokens** - clean up old tokens regularly

## ✅ Success Checklist

- [ ] GitHub MCP server installed globally
- [ ] MCP configuration added to Claude Code settings
- [ ] GitHub Personal Access Token created
- [ ] Environment variable `GITHUB_TOKEN` set
- [ ] Claude Code restarted
- [ ] MCP server responding to help command

Your GitHub MCP is now ready to use with Claude Code! 🎉