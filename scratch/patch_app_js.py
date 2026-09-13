# -*- coding: utf-8 -*-
import sys, io

def patch():
    with open('Wiki/app.js', 'r', encoding='utf-8') as f:
        app_js = f.read()

    with open('scratch/perfect_engine.js', 'r', encoding='utf-8') as f:
        engine_code = f.read()

    # 1. Patch postprocessHtml to count mermaid diagrams and pass diagramIndexInDoc
    target_post = r'''    const codeBlockRegex = /<pre><code(?:\s+class="([^"]*)")?>([\s\S]*?)<\/code><\/pre>/g;
    result = result.replace(codeBlockRegex, (match, classAttr, codeContent) => {
      const langMatch = (classAttr || '').match(/language-([a-zA-Z0-9_-]+)/);
      const lang = langMatch ? langMatch[1].toLowerCase() : 'text';

      if (lang === 'mermaid') {
        const decodedCode = unescapeHtml(codeContent.trim());
        const nativeVisual = buildNativeDsaVisual(decodedCode, state.currentDoc ? state.currentDoc.id : '');'''

    replace_post = r'''    let diagramIndexInDoc = 0;
    const codeBlockRegex = /<pre><code(?:\s+class="([^"]*)")?>([\s\S]*?)<\/code><\/pre>/g;
    result = result.replace(codeBlockRegex, (match, classAttr, codeContent) => {
      const langMatch = (classAttr || '').match(/language-([a-zA-Z0-9_-]+)/);
      const lang = langMatch ? langMatch[1].toLowerCase() : 'text';

      if (lang === 'mermaid') {
        diagramIndexInDoc++;
        const decodedCode = unescapeHtml(codeContent.trim());
        const nativeVisual = buildNativeDsaVisual(decodedCode, state.currentDoc ? state.currentDoc.id : '', diagramIndexInDoc);'''

    if target_post not in app_js:
        print("ERROR: target_post not found in Wiki/app.js")
        return False
    app_js = app_js.replace(target_post, replace_post, 1)

    # 2. Patch buildNativeDsaVisual function
    # Find start: function buildNativeDsaVisual(code, docId) {
    # Find end: return generateGenericDsaLabVisual(code, getArchitectureTitle(code));\n  }
    start_str = "  function buildNativeDsaVisual(code, docId) {"
    end_str = "    return generateGenericDsaLabVisual(code, getArchitectureTitle(code));\n  }"

    s_idx = app_js.find(start_str)
    if s_idx == -1:
        print("ERROR: start_str not found in Wiki/app.js")
        return False
    e_idx = app_js.find(end_str, s_idx)
    if e_idx == -1:
        print("ERROR: end_str not found in Wiki/app.js")
        return False
    e_idx += len(end_str)

    # Replace from s_idx to e_idx with engine_code
    new_app_js = app_js[:s_idx] + engine_code.strip() + app_js[e_idx:]

    with open('Wiki/app.js', 'w', encoding='utf-8') as f:
        f.write(new_app_js)

    print("Wiki/app.js successfully patched with perfect visualizer engine!")
    return True

if __name__ == '__main__':
    patch()
