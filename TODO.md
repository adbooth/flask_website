1. Use global objects for templates
2. Clean up JS and CSS
3. Clean up everything
4. Improve the README
5. Improve the content lists
6. Mobile improvements


g.project_mu = {fn.replace('.md', ''): Markup(markdown(open(os.path.join(paths['projects'], fn)).read())) for fn in os.listdir(paths['projects']) if fn.endswith('.md')}
