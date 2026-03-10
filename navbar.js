const NAV_ITEMS = [
  { id: 'home',         href: 'index.html',        icon: 'fa-home',        label: 'HOME' },
  { id: 'research',     href: 'files/research.html', icon: 'fa-search',    label: 'RESEARCH' },
  { id: 'teaching',     href: 'files/teaching.html', icon: 'fa-book',      label: 'TEACHING' },
  { id: 'cv',           href: 'files/cv.html',       icon: 'fa-user',      label: 'CV' },
  { id: 'publications', href: 'files/publications.html', icon: 'fa-scroll', label: 'PUBLICATIONS' },
  { id: 'contact',      href: 'files/contact.html',  icon: 'fa-envelope',  label: 'CONTACT' },
];

// Appeler dans chaque page : loadNavbar('research')
async function loadNavbar(activePage, rootPath = '../') {
  const res = await fetch(rootPath + 'navbar.html');
  let html = await res.text();
  html = html.replaceAll('{ROOT}', rootPath);
  document.getElementById('navbar-placeholder').innerHTML = html;

  // Injecter les liens nav avec le bon actif
  const container = document.getElementById('nav-links');
  NAV_ITEMS.forEach(item => {
    const isActive = item.id === activePage;
    const href = item.id === 'home' ? rootPath + 'index.html'
                  : rootPath + item.href;
    container.innerHTML += `
      <a href="${href}"
         class="w3-bar-item w3-button nav-button w3-padding-large
                ${isActive ? 'w3-white' : ''}"
         ${isActive ? 'style="color:var(--primary-color)!important;"' : ''}
         aria-current="${isActive ? 'page' : 'false'}">
        <i class="fa ${item.icon}"></i> ${item.label}
      </a>`;
  });
}
