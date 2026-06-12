## Task 21
Open *styles.css* in your text editor. Add the following comment and style rules after the style rule for `img` and `video`:
```css
/* Style rules for skip navigation link */
.skip {
    position: absolute;
    left: -999px;
}

.skip:focus {
    color: #fff;
    background-color: #2a1f14;
    text-decoration: none;
    padding: 0.5%;
    top: auto;
    left: auto;
    right: 1px;
    z-index: 1;
}
```