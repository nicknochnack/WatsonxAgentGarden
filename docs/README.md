# Documentation

This directory contains the Jekyll-based documentation site for the Watsonx Agent Garden 🪴.

## 🌐 Live Site

The documentation site is available at: `https://nicknochnack.github.io/WatsonxAgentGarden`

## 📁 Structure

```
docs/
├── _config.yml              # Jekyll configuration
├── _layouts/
│   └── default.html         # Custom layout with navigation
├── index.md                 # Course homepage
├── orchestrate.md           # Chapter 1: No-code with Orchestrate
├── langflow.md              # Chapter 2: Low-code with Langflow
├── langgraph.md             # Chapter 3: Pro-code with Langgraph
├── governance.md            # Chapter 4: AI Governance
├── Gemfile                  # Ruby dependencies
└── README.md               # This file
```

## 🚀 Local Development

To run the site locally:

1. **Install Jekyll**:
   ```bash
   gem install bundler jekyll
   ```

2. **Install dependencies**:
   ```bash
   cd docs
   bundle install
   ```

3. **Serve locally**:
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**:
   Open `http://localhost:4000` in your browser

## 🔧 GitHub Pages Setup

The site is automatically deployed using GitHub Actions:

1. **Workflow**: `.github/workflows/deploy.yml`
2. **Source**: `docs/` directory
3. **Trigger**: Push to `main` branch
4. **Theme**: Minima (Jekyll default theme)

## 📝 Adding Content

### Adding Video Embeds

To replace video placeholders with actual videos:

1. **YouTube**: Replace the placeholder div with:
   ```html
   <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" 
           title="YouTube video player" frameborder="0" allowfullscreen></iframe>
   ```

2. **Vimeo**: Replace with:
   ```html
   <iframe src="https://player.vimeo.com/video/VIDEO_ID" width="560" height="315" 
           frameborder="0" allowfullscreen></iframe>
   ```

### Adding New Sections

1. Create a new `.md` file in the `docs/` directory
2. Add front matter:
   ```yaml
   ---
   layout: default
   title: "Chapter X: Title"
   ---
   ```
3. Update `_config.yml` to include the new section in the course structure

### Customizing Styling

- Modify `_layouts/default.html` for layout changes
- Add custom CSS in the `<style>` section of individual pages
- Override theme styles by creating `_sass/` directory with custom SCSS

## 🎨 Features

### Navigation
- **Course navigation bar** on all chapter pages
- **Previous/Next links** for sequential navigation
- **Home button** to return to course overview

### Responsive Design
- **Mobile-friendly** navigation and layout
- **Grid-based** course section cards
- **Flexible** video placeholders

### Course Structure
- **Progressive learning path** from no-code to pro-code
- **Clear learning objectives** for each chapter
- **Practical exercises** and code examples
- **Resource links** for deeper learning

## 🔄 Updating Content

The site automatically rebuilds when you:
1. Push changes to the `main` branch
2. Modify any file in the `docs/` directory
3. Update the course structure in `_config.yml`

Changes typically take 1-2 minutes to appear on the live site.

## 🐛 Troubleshooting

### Build Failures
- Check the Actions tab on GitHub for build errors
- Ensure all Markdown syntax is valid
- Verify Jekyll front matter is correctly formatted

### Local Development Issues
- Run `bundle update` to update dependencies
- Check Ruby version compatibility (3.1+ recommended)
- Clear Jekyll cache with `bundle exec jekyll clean`

### Navigation Issues
- Verify section titles match between `_config.yml` and page front matter
- Check that all linked files exist and have correct extensions

## 📧 Support

For issues with the documentation site:
1. Check the GitHub Actions build logs
2. Review Jekyll documentation: https://jekyllrb.com/docs/
3. Test changes locally before pushing
4. Reach out during course sessions for help 