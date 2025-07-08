#!/usr/bin/env python3
"""
Generate a custom GitHub-style contribution grid SVG with full year layout
"""
import random

def generate_contribution_grid():
    """Generate SVG for GitHub-style contribution grid"""
    
    # SVG dimensions and colors
    width = 1000
    height = 180
    colors = {
        'bg': '#2c2b25',
        'text': '#9ca3af',
        'level0': '#161b22',  # No contributions
        'level1': '#0e4429',  # Low contributions
        'level2': '#006d32',  # Medium-low contributions
        'level3': '#26a641',  # Medium-high contributions
        'level4': '#39d353'   # High contributions
    }
    
    # Months and days
    months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    days = ['', 'Mon', '', 'Wed', '', 'Fri', '']
    
    # Start SVG
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="{colors['bg']}"/>
  
  <!-- Month Labels -->'''
    
    # Add month labels
    for i, month in enumerate(months):
        x = 80 + (i * 75)
        svg += f'\n  <text x="{x}" y="25" fill="{colors["text"]}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="12" text-anchor="middle">{month}</text>'
    
    # Add day labels
    svg += '\n  \n  <!-- Day Labels -->'
    for i, day in enumerate(days):
        if day:
            y = 50 + (i * 15)
            svg += f'\n  <text x="35" y="{y}" fill="{colors["text"]}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="12" text-anchor="end">{day}</text>'
    
    # Generate contribution grid
    svg += '\n  \n  <!-- Contribution Grid -->\n  <g transform="translate(50, 35)">'
    
    # Generate 53 weeks × 7 days
    weeks = 53
    days_per_week = 7
    
    for week in range(weeks):
        for day in range(days_per_week):
            x = week * 15
            y = day * 15
            
            # Generate realistic contribution pattern
            # More activity in recent weeks
            if week < 20:  # Early months - low activity
                level = random.choices([0, 1], weights=[85, 15])[0]
            elif week < 40:  # Middle months - moderate activity
                level = random.choices([0, 1, 2], weights=[70, 20, 10])[0]
            else:  # Recent months - higher activity
                level = random.choices([0, 1, 2, 3, 4], weights=[40, 25, 20, 10, 5])[0]
            
            color = f"level{level}"
            svg += f'\n    <rect x="{x}" y="{y}" width="11" height="11" fill="{colors[color]}" rx="2"/>'
    
    svg += '\n  </g>'
    
    # Add legend
    svg += f'''
  
  <!-- Legend -->
  <g transform="translate(720, 155)">
    <text x="0" y="12" fill="{colors["text"]}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="12">Less</text>
    <rect x="30" y="2" width="11" height="11" fill="{colors["level0"]}" rx="2"/>
    <rect x="45" y="2" width="11" height="11" fill="{colors["level1"]}" rx="2"/>
    <rect x="60" y="2" width="11" height="11" fill="{colors["level2"]}" rx="2"/>
    <rect x="75" y="2" width="11" height="11" fill="{colors["level3"]}" rx="2"/>
    <rect x="90" y="2" width="11" height="11" fill="{colors["level4"]}" rx="2"/>
    <text x="110" y="12" fill="{colors["text"]}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="12">More</text>
  </g>
</svg>'''
    
    return svg

if __name__ == "__main__":
    svg_content = generate_contribution_grid()
    with open("contribution-grid.svg", "w") as f:
        f.write(svg_content)
    print("Generated contribution-grid.svg")