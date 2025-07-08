# Claymorphism GitHub Profile Setup Instructions

## Quick Setup Guide

### 1. Create Your Profile Repository
1. Go to GitHub and create a new repository
2. **Repository name must be exactly your GitHub username**
3. Make sure it's **public**
4. Initialize with README (or use the one provided)

### 2. Customize Your Profile
Replace the following placeholders in the README.md:

- `[Your Name]` - Your actual name
- `YOUR_USERNAME` - Your GitHub username
- `your.email@example.com` - Your email address
- `YOUR_LINKEDIN` - Your LinkedIn profile URL
- `YOUR_TWITTER` - Your Twitter handle
- Update the typing animation text to match your role/skills

### 3. Set Up GitHub Actions for Snake Animation (Optional)
1. Create `.github/workflows/snake.yml` in your profile repository
2. Add the following workflow:

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
          github_user_name: YOUR_USERNAME
          outputs: dist/github-contribution-grid-snake.svg

      - name: Push snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v2.6.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 4. Technology Badges
The profile uses soft, clay-inspired badges with:
- **Flat style** instead of harsh for-the-badge
- **Soft colors** with muted tones
- **Light backgrounds** (#f7f7f7) for gentle contrast
- You can customize colors and add new badges from [shields.io](https://shields.io/)

### 5. Claymorphism Design Elements
The profile features:
- **Soft gradients** with pastel color combinations
- **Rounded corners** (20-30px border radius)
- **Subtle shadows** with low opacity
- **Backdrop blur effects** for depth
- **Gentle color transitions** throughout sections

## Color Palette (Claymorphism Theme)
The profile uses a soft, clay-inspired color scheme:
- **Primary Text**: `#8B7355` (Warm brown)
- **Secondary Text**: `#6B7280` (Soft gray)
- **Accent Color**: `#D4A574` (Warm beige)
- **Background Gradients**: 
  - Light pastels: `#f5f7fa` to `#c3cfe2`
  - Warm tones: `#ffecd2` to `#fcb69f`
  - Cool tones: `#a8edea` to `#fed6e3`
  - Purple blend: `#667eea` to `#764ba2`

## Design Principles
- **Soft Shadows**: `0 15px 35px rgba(0,0,0,0.1)`
- **Blur Effects**: `backdrop-filter: blur(10px)`
- **Rounded Elements**: `border-radius: 25px`
- **Gentle Typography**: Plus Jakarta Sans with controlled spacing
- **Subtle Animations**: Smooth transitions and hover effects

### 6. Personal Touch
- Update the about section with your actual information
- Change the quote at the bottom to something that resonates with you
- Customize gradient colors to match your preferences
- Add any additional sections that showcase your personality

### 7. Advanced Features (Optional)
- Add more clay-like sections with different gradient combinations
- Include custom SVG icons with soft shadows
- Create animated elements with gentle transitions
- Add interactive hover effects

## Browser Compatibility
The claymorphism effects work best in:
- ✅ Chrome/Edge (full support)
- ✅ Firefox (good support)
- ✅ Safari (good support)
- ⚠️ Older browsers may not show all effects

## Tips for Claymorphism Design
- Keep shadows subtle and soft
- Use muted, pastel colors
- Apply gentle blur effects
- Maintain good contrast for readability
- Test on different devices and screen sizes
- Consider accessibility with sufficient color contrast

## Common Issues
- If gradients don't show, check browser compatibility
- Some blur effects might not work on all GitHub themes
- Profile stats colors can be customized with URL parameters
- Snake animation requires GitHub Actions to be enabled

Your clay-inspired profile is now ready to showcase your unique style! 🎨