# Jekyll Two-Column Layout Prompt

Create a Jekyll layout with a two-column design: a collapsible left sidebar (50px when collapsed, 300px when expanded) and a main content area that adjusts accordingly.

## Requirements

**Layout Structure:**
- Use CSS Grid with `grid-template-columns` transitioning between `50px 1fr` (collapsed) and `300px 1fr` (expanded)
- The sidebar should be `position: sticky; top: 0; height: 100vh; overflow-y: auto;`
- The main content should have `min-width: 0` to prevent overflow

**Sidebar Behavior:**
- Default state: collapsed to 50px width
- Toggle button (an "ear" on the sidebar) switches between collapsed/expanded states
- When collapsed: show only the toggle button
- When expanded: show sidebar content
- Toggle button shows `▶` when collapsed, `◀` when expanded
- Use a `.sidebar-expanded` class on the wrapper to control the expanded state

**HTML Structure:**
```html
<div class="layout-wrapper">
  <aside class="sidebar">
    <button class="sidebar-toggle" onclick="document.querySelector('.layout-wrapper').classList.toggle('sidebar-expanded')"></button>
    <div class="sidebar-brand">
      {brand}
    </div>
    <nav class="sidebar-nav">
      <!-- navigation items -->
    </nav>
  </aside>
  <main class="main-content">
    {{ content }}
  </main>
</div>
```

**CSS Requirements:**
- Smooth transition for grid column changes (0.2s ease)
- Sidebar background: #f5f5f5, border-right: 1px solid #ddd
- Toggle button: centered, 40px height, full width, border 1px solid #ccc
- Mobile responsive: below 720px, sidebar becomes fixed overlay with transform
- Preserve all existing typography, code blocks, and letter styles

**JavaScript:**
- Simple class toggle on `.layout-wrapper` - no external dependencies
