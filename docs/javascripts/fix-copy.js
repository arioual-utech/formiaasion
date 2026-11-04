// Après déchiffrement, tous les blocs de code ont le même id : chaque bouton « copier » vise alors le premier bloc.
// On redonne un id unique à chaque bloc et on repointe son bouton.
function fixCodeIds() {
  document.querySelectorAll(".md-typeset .highlight pre").forEach((pre, i) => {
    const id = "__code_" + i;
    if (pre.id === id) return;
    pre.id = id;
    const bouton = pre.querySelector(".md-code__button");
    if (bouton) bouton.setAttribute("data-clipboard-target", "#" + id + " > code");
  });
}

new MutationObserver(fixCodeIds).observe(document.body, { childList: true, subtree: true });
fixCodeIds();
