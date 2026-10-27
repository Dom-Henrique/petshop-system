// Abre e fecha o menu no celular (botão .menu dentro de .nav-bar)
const navBar = document.querySelector('.nav-bar');
const botaoMenu = document.querySelector('.menu');

if (navBar && botaoMenu) {
  const icone = botaoMenu.querySelector('i');

  botaoMenu.addEventListener('click', () => {
    const aberto = navBar.classList.toggle('open');

    botaoMenu.setAttribute('aria-expanded', String(aberto));
    botaoMenu.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
    icone.className = aberto ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
  });
}