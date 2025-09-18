document.addEventListener('DOMContentLoaded', function () {

    // Modal
    const modal = document.getElementById('modal-produto');
    const btnsLeiaMais = document.querySelectorAll('.btn-leia-mais');
    const spanFechar = document.querySelector('.fechar');

    // Abrir modal
    btnsLeiaMais.forEach(btn => {
        btn.addEventListener('click', function () {
            const nome = this.getAttribute('data-nome');
            const descricao = this.getAttribute('data-descricao');
            const preco = parseFloat(this.getAttribute('data-preco'));
            const promocao = parseFloat(this.getAttribute('data-promocao'));
            const emPromocao = this.getAttribute('data-em-promocao') === "true";
            const imagem = this.getAttribute('data-imagem');

            // Preencher conteúdo do modal
            document.getElementById('modal-nome').textContent = nome;
            document.getElementById('modal-descricao').textContent = descricao;
            document.getElementById('modal-imagem').src = imagem;

            const precoContainer = document.getElementById('modal-preco');

            // Verifica se há promoção
            if (emPromocao && promocao) {
                // Calcula % de desconto
                const desconto = ((preco - promocao) / preco * 100).toFixed(0);

                precoContainer.innerHTML = `
                    <span style="text-decoration: line-through; color: #888; margin-right: 8px;">
                        R$ ${preco.toFixed(2)}
                    </span>
                    <span style="color: #d32f2f; font-weight: bold; font-size: 1.2em;">
                        R$ ${promocao.toFixed(2)}
                    </span>
                    <span style="background: #ff5252; color: #fff; padding: 2px 6px; border-radius: 4px; margin-left: 8px; font-size: 0.9em;">
                        -${desconto}%
                    </span>
                `;
            } else {
                precoContainer.innerHTML = `
                    <span style="font-weight: bold; font-size: 1.1em;">
                        R$ ${preco.toFixed(2)}
                    </span>
                `;
            }

            // Exibir modal
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden'; // Desabilita o scroll quando o modal está aberto
        });
    });

    // Fechar modal
    if (spanFechar) {
        spanFechar.onclick = function () {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        };
    }

    // Fechar modal clicando fora do modal
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    };

    // Fechar modal com a tecla ESC
    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Alternar tema
    const toggleTemaBtn = document.querySelector('.toggle-tema button');

    // Verifica se o botão de alternar tema existe antes de adicionar o evento
    if (toggleTemaBtn) {
        // Verifica se o tema está armazenado no localStorage
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme) {
            document.body.classList.add(storedTheme);
        } else {
            const systemPreference = window.matchMedia('(prefers-color-scheme: dark)').matches;
            document.body.classList.add(systemPreference ? 'dark-mode' : 'light-mode');
        }

        toggleTemaBtn.addEventListener('click', function () {
            if (document.body.classList.contains('dark-mode')) {
                document.body.classList.remove('dark-mode');
                document.body.classList.add('light-mode');
                localStorage.setItem('theme', 'light-mode');
            } else {
                document.body.classList.remove('light-mode');
                document.body.classList.add('dark-mode');
                localStorage.setItem('theme', 'dark-mode');
            }
        });
    }

});
