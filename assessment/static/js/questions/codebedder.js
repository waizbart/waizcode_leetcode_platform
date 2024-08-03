(() => {
    if (window.CodeBedder) return;
  
    class CodeBedder extends HTMLElement {
      static register(tagName = 'code-bedder') {
        window.customElements.define(tagName, CodeBedder);
      }
  
      static formAssociated = true;
  
      static style = `
  code-bedder,
  code-bedder pre,
  code-bedder code,
  code-bedder textarea {
    box-sizing: border-box;
  }
  
  code-bedder {
    --code-bedder-tab-size: 2;
    --code-bedder-font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    --code-bedder-font-size: 14px;
    --code-bedder-caret-color: white;
    --code-bedder-selection-background: hsla(0, 0%, 100%, 0.2);
  
    --code-bedder-scrollbar-size: 0.5rem;
    --code-bedder-scrollbar-radius: 0.25rem;
    --code-bedder-scrollbar-track-background: hsl(215, 19%, 35%);
    --code-bedder-scrollbar-thumb-background: hsl(215, 16%, 47%);
    --code-bedder-scrollbar-thumb-hover-background: hsl(215, 20%, 65%);
  
    overflow: hidden;
    position: relative;
    font-size: var(--code-bedder-font-size);
    background-color: hsl(70, 8%, 15%);
  }
  
  code-bedder pre,
  code-bedder code,
  code-bedder textarea {
    tab-size: var(--code-bedder-tab-size) !important;
  }
  
  code-bedder pre,
  code-bedder textarea {
    outline: 0;
    border-radius: 0;
  }
  
  code-bedder pre {
    width: 100%;
    height: 100%;
    margin: 0 !important;
    padding: 0 !important;
  }
  
  code-bedder code,
  code-bedder textarea {
    outline: 0;
    font-family: var(--code-bedder-font-family);
    font-size: 1em;
    line-height: 1.5;
  }
  
  code-bedder code {
    display: block;
  }
  
  code-bedder textarea {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    resize: none;
    margin: 0;
    margin-bottom: -2px; /* fixes scrollbar when using auto height */
    padding: 0;
    background: transparent;
    color: transparent;
    white-space: pre;
    caret-color: var(--code-bedder-caret-color);
  }
  
  code-bedder textarea::selection {
    background-color: var(--code-bedder-selection-background);
  }
  
  /* Scrollbars */
  code-bedder pre::-webkit-scrollbar {
    width: 0.5rem;
    height: 0.5rem;
  }
  
  code-bedder pre::-webkit-scrollbar-track,
  code-bedder pre::-webkit-scrollbar-thumb,
  code-bedder pre::-webkit-scrollbar-thumb:hover {
    background-color: transparent;
  }
  
  code-bedder textarea::-webkit-scrollbar {
    width: var(--code-bedder-scrollbar-size);
    height: var(--code-bedder-scrollbar-size);
  }
  
  code-bedder textarea::-webkit-scrollbar-track {
    background-color: var(--code-bedder-scrollbar-track-background);
  }
  
  code-bedder textarea::-webkit-scrollbar-thumb {
    border-radius: var(--code-bedder-scrollbar-radius);
    background-color: var(--code-bedder-scrollbar-thumb-background);
  }
  
  code-bedder textarea::-webkit-scrollbar-thumb:hover {
    border-radius: var(--code-bedder-scrollbar-radius);
    background-color: var(--code-bedder-scrollbar-thumb-hover-background);
  }
  `;
  
      events = {};
  
      constructor() {
        super();
        this.internals = this.attachInternals();
      }
  
      connectedCallback() {
        setTimeout(() => this.render(), 0);
      }
  
      render() {
        const container = this;
  
        const codeContent = this.textContent;
        this.textContent = '';
  
        const style = document.createElement('style');
        style.textContent = CodeBedder.style;
        this.appendChild(style);
  
        const pre = document.createElement('pre');
        const code = document.createElement('code');
        code.textContent = codeContent;
        code.className = `language-${this.getAttribute('data-language') || 'html'}`;
        pre.appendChild(code);
        this.appendChild(pre);
  
        this.textarea = document.createElement('textarea');
        this.textarea.setAttribute('spellcheck', false);
        this.textarea.value = codeContent;
        this.textarea.name = "answer";
        this.appendChild(this.textarea);
  
        this.textarea.addEventListener('input', function () {
          container.internals.setFormValue(this.value);
  
          // pre ignores an empty new line at the end which breaks scrolling - an extra character fixes it
          code.textContent = this.value + (this.value.endsWith('\n') ? ' ' : '');
  
          if (container.getAttribute('onhighlight')) {
            (function () {
              eval(container.getAttribute('onhighlight'));
            }).call(code);
          }
        });
  
        this.textarea.addEventListener('scroll', function () {
          pre.scrollLeft = this.scrollLeft;
          pre.scrollTop = this.scrollTop;
        });
  
        this.events.load = true;
        this.dispatchEvent(new Event('load'));
        this.textarea.dispatchEvent(new Event('input'));
      }
  
      // Event handling
      on(...args) {
        const [eventName, callback] = args;
        if (this.events[eventName]) {
          callback.call(this);
        } else {
          this.addEventListener(...args);
        }
      }
  
      off(...args) {
        this.removeEventListener(...args);
      }
  
      // Properties
      get value() {
        return this.textarea?.value;
      }
  
      set value(value) {
        this.textarea.value = value;
      }
    }
  
    if (!document.currentScript.hasAttribute('data-manual')) {
      CodeBedder.register();
    }
  
    window.CodeBedder = CodeBedder;
  })();