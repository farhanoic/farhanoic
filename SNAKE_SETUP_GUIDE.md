# 🐍 Snake Animation Setup Guide

## Step-by-Step Instructions

### Step 1: Create Your Profile Repository

1. **Go to GitHub.com** and make sure you're logged in
2. **Click the "+" icon** in the top-right corner
3. **Select "New repository"**
4. **Repository name**: Must be exactly `farhanoic` (your username)
5. **Description**: "My GitHub Profile"
6. **Make it Public** ✅
7. **Add README file** ✅
8. **Click "Create repository"**

### Step 2: Upload Your README

1. **In your new repository**, click "Upload files" or use the file editor
2. **Replace the default README.md** with the claymorphism README I created
3. **Commit the changes** with message: "Add claymorphism profile design"

### Step 3: Set Up GitHub Actions Workflow

#### Option A: Using GitHub Web Interface (Recommended)

1. **In your `farhanoic` repository**, click the "Actions" tab
2. **Click "New workflow"**
3. **Click "set up a workflow yourself"**
4. **Replace the default content** with the snake workflow code
5. **Name the file**: `snake.yml`
6. **Click "Start commit"**
7. **Add commit message**: "Add snake animation workflow"
8. **Click "Commit new file"**

#### Option B: Manual File Creation

1. **In your repository**, click "Create new file"
2. **Type the path**: `.github/workflows/snake.yml`
   - GitHub will automatically create the folders
3. **Paste the snake workflow code** (provided below)
4. **Commit the file**

### Step 4: Snake Workflow Code

```yaml
name: Generate Snake Animation

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  schedule:
    # Runs every 6 hours
    - cron: "0 */6 * * *"
  
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
  
  # Also run on push to main branch
  push:
    branches: [ main ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
    
    # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
    - uses: actions/checkout@v3
    
    # Generates the snake  
    - uses: Platane/snk@v3
      id: snake-gif
      with:
        github_user_name: farhanoic
        # these next 2 lines generate the files on a branch called "output". This keeps the main branch from cluttering up.
        gif_out_path: dist/github-contribution-grid-snake.gif
        svg_out_path: dist/github-contribution-grid-snake.svg

    # show the status of the build. Makes it easier for debugging (if there's any issues).
    - run: git status

    # Push the changes
    - name: Push changes
      uses: ad-m/github-push-action@v0.6.0
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        branch: output
        force: true

    - uses: crazy-max/ghaction-github-pages@v3.1.0
      with:
        target_branch: output
        build_dir: dist
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Step 5: Enable GitHub Actions

1. **Go to your repository Settings**
2. **Scroll to "Actions"** in the left sidebar
3. **Click "General"**
4. **Under "Actions permissions"**, select:
   - ✅ "Allow all actions and reusable workflows"
5. **Under "Workflow permissions"**, select:
   - ✅ "Read and write permissions"
   - ✅ "Allow GitHub Actions to create and approve pull requests"
6. **Click "Save"**

### Step 6: Run the Workflow

#### Manual Trigger (Immediate)
1. **Go to "Actions" tab** in your repository
2. **Click "Generate Snake Animation"** workflow
3. **Click "Run workflow"** dropdown
4. **Click "Run workflow"** button
5. **Wait for the green checkmark** (usually 1-2 minutes)

#### Automatic Trigger
- The workflow will run automatically:
  - Every 6 hours
  - When you push to main branch
  - When you make contributions

### Step 7: Verify It's Working

1. **Check the Actions tab** for green checkmarks
2. **Look for a new branch** called `output` in your repository
3. **Check your profile** - the snake should appear within a few minutes
4. **If it doesn't work**, check the troubleshooting section below

## 🔧 Troubleshooting

### Common Issues

#### 1. **Workflow Failed**
- **Check Actions tab** for error messages
- **Most common fix**: Update workflow permissions (Step 5)
- **Alternative**: Try using the latest action version

#### 2. **Snake Not Appearing**
- **Wait 5-10 minutes** after successful workflow run
- **Check if `output` branch exists** with the snake files
- **Verify the image path** in your README matches: `https://github.com/farhanoic/farhanoic/blob/output/github-contribution-grid-snake.svg`

#### 3. **Permission Denied**
- **Go to Settings → Actions → General**
- **Enable "Read and write permissions"**
- **Enable "Allow GitHub Actions to create and approve pull requests"**

#### 4. **No Contributions to Animate**
- **Make some commits** to any repository
- **The snake needs contributions** to create the animation
- **Wait for the workflow to run again**

### Alternative Workflow (If Above Doesn't Work)

```yaml
name: Generate Snake

on:
  schedule:
    - cron: "0 */6 * * *"
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Generate snake.svg
        uses: Platane/snk/svg-only@v2
        with:
          github_user_name: farhanoic
          outputs: dist/github-contribution-grid-snake.svg

      - name: Push snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v2.6.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 📝 Important Notes

- **Repository name** must exactly match your username: `farhanoic`
- **Repository must be public** for the profile to show
- **First run might take longer** as GitHub sets up the workflow
- **Snake animation updates** every 6 hours automatically
- **You can manually trigger** the workflow anytime from Actions tab

## ✅ Success Checklist

- [ ] Repository named `farhanoic` created
- [ ] README.md uploaded with claymorphism design
- [ ] Snake workflow file in `.github/workflows/snake.yml`
- [ ] GitHub Actions enabled with proper permissions
- [ ] Workflow ran successfully (green checkmark)
- [ ] `output` branch created with snake files
- [ ] Snake animation visible on your profile

## 🎉 Final Result

Once everything is set up correctly, you'll have:
- A beautiful claymorphism-themed profile
- Auto-updating GitHub stats
- An animated snake that eats your contributions
- A profile that updates automatically every 6 hours

The snake will create a visual representation of your GitHub activity, making your profile more engaging and dynamic!