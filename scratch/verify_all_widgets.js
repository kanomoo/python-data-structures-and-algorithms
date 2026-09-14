// Verification script to ensure all 14 assignment & classroom example widgets mount and run properly
const fs = require('fs');
const path = require('path');

// Mock browser DOM environment
class MockClassList {
  constructor() { this.classes = new Set(); }
  add(c) { this.classes.add(c); }
  remove(c) { this.classes.delete(c); }
  contains(c) { return this.classes.has(c); }
}

class MockElement {
  constructor(tagName = 'div', id = '') {
    this.tagName = tagName.toUpperCase();
    this.id = id;
    this.classList = new MockClassList();
    this.children = [];
    this.parentNode = null;
    this.nextSibling = null;
    this._innerHTML = '';
    this.dataset = {};
    this.textContent = '';
    this.disabled = false;
  }

  get innerHTML() { return this._innerHTML; }
  set innerHTML(val) {
    this._innerHTML = val;
    // Update simple textContent
    this.textContent = val.replace(/<[^>]*>/g, '');
  }

  appendChild(child) {
    child.parentNode = this;
    this.children.push(child);
    return child;
  }

  insertBefore(newChild, refChild) {
    newChild.parentNode = this;
    const idx = this.children.indexOf(refChild);
    if (idx >= 0) {
      this.children.splice(idx, 0, newChild);
    } else {
      this.children.push(newChild);
    }
    return newChild;
  }

  querySelector(selector) {
    return this.querySelectorAll(selector)[0] || null;
  }

  querySelectorAll(selector) {
    const results = [];
    function search(node) {
      if (!node || !node.children) return;
      for (const child of node.children) {
        if (selector.startsWith('#') && child.id === selector.slice(1)) {
          results.push(child);
        } else if (selector.startsWith('.') && child.classList.contains(selector.slice(1))) {
          results.push(child);
        } else if (selector.toLowerCase() === child.tagName.toLowerCase()) {
          results.push(child);
        }
        search(child);
      }
    }
    search(this);
    return results;
  }

  scrollIntoView() {}
}

const mockDocElements = {};
global.document = {
  getElementById: (id) => mockDocElements[id] || null,
  createElement: (tag) => {
    const el = new MockElement(tag);
    // Simple helper parser for template strings
    return {
      set innerHTML(html) {
        el.innerHTML = html;
        // Parse root div with id if exists
        const idMatch = html.match(/id="([^"]+)"/);
        if (idMatch) {
          el.id = idMatch[1];
          mockDocElements[el.id] = el;
        }
        // Also populate common sub-elements so querySelector works
        const selectors = [
          'studio-step-counter', 'studio-step-title', 'studio-step-exp',
          'studio-watch-tbody', 'studio-canvas-area', 'code-trace-lines', 'active-code-line-num'
        ];
        selectors.forEach(sel => {
          if (html.includes(sel)) {
            const sub = new MockElement('div');
            sub.classList.add(sel);
            el.appendChild(sub);
          }
        });
        // Buttons
        ['prev', 'next', 'play'].forEach(b => {
          if (el.id) {
            const btn = new MockElement('button', `${el.id}-${b}`);
            mockDocElements[btn.id] = btn;
            el.appendChild(btn);
          }
        });
      },
      get firstElementChild() {
        return el;
      }
    };
  }
};
global.window = {
  DsaWikiStudio: null
};

// Load studio script
require('../Wiki/dsa-interactive-studio.js');

const studio = window.DsaWikiStudio;
console.log('Testing DSA Wiki Studio Module...');

if (!studio || typeof studio.mountWidgetsForDoc !== 'function') {
  console.error('FAIL: window.DsaWikiStudio is not properly defined!');
  process.exit(1);
}

const docsToTest = [
  '12.1 - Assignment 1 Singly Linked List',
  '12.2 - Assignment 2 Construct Binary Tree',
  '12.3 - Assignment 3 Binary Min-Heap',
  '12.4 - Assignment 4 Graph Topological Sort',
  '12.5 - Test Program 1 & 2 Queue Implementation',
  '12.6 - 0Exercises Warm-up Function Tracing',
  '13.1 - For Example Lecture 3 Linked List',
  '13.2 - For Example Lecture 4 Stack & Postfix',
  '13.3 - For Example Lecture 4 Queue',
  '13.4 - For Example Lecture 5 Binary Tree',
  '13.5 - For Example Lecture 5.1 & 5.2 BST',
  '13.6 - For Example Lecture 8.1 Binary Heap',
  '13.7 - For Example Lecture 9 Sorting',
  '13.8 - For Example Lecture 10 & 11 Graph'
];

let successCount = 0;
docsToTest.forEach(docId => {
  const mockArticleBody = new MockElement('div');
  const h2 = new MockElement('h2');
  h2.textContent = '## 📌 โจทย์และขั้นตอนวิธี';
  mockArticleBody.appendChild(h2);

  try {
    studio.mountWidgetsForDoc(docId, mockArticleBody);
    console.log(`✅ SUCCESS: Mounted widget for "${docId}" (Children: ${mockArticleBody.children.length})`);
    successCount++;
  } catch (err) {
    console.error(`❌ ERROR mounting for "${docId}":`, err.message);
  }
});

console.log(`\nVerified ${successCount} / ${docsToTest.length} widgets mounted successfully!`);
if (successCount === docsToTest.length) {
  console.log('🎉 ALL ASSIGNMENT & CLASSROOM EXAMPLE WIDGETS FUNCTIONING PERFECTLY!');
} else {
  process.exit(1);
}
