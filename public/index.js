let home_memes = [];

// Fetch the memes and render only after the response arrives
// we also render a download button and the meme name with the name's '_' replaced with ' '
fetch('/home')
    .then(response => response.json())
    .then(data => {
        home_memes = data.memes || [];
        renderMemes(home_memes);
    })
    .catch(err => {
        console.error('Failed to load memes:', err);
    });

// Render helper
function renderMemes(memes) {
    const memesContainer = document.getElementById('memes-container');
    memesContainer.innerHTML = '';
        if (!memes || memes.length === 0) {
            memesContainer.innerHTML = '<p class="loading">No memes found.</p>';
            return;
        }

        memes.forEach(meme => {
            const card = document.createElement('div');
            card.className = 'meme-item';

            const img = document.createElement('img');
            img.src = `/sendmeme?meme=${encodeURIComponent(meme.name)}`;
            img.alt = meme.name;

            const content = document.createElement('div');
            content.className = 'meme-content';

            const title = document.createElement('div');
            title.className = 'meme-title';
            title.textContent = meme.name;

            const desc = document.createElement('div');
            desc.className = 'meme-description';
            desc.textContent = meme.category || '';

            const actions = document.createElement('div');
            actions.className = 'meme-actions';
            const downloadBtn = document.createElement('button');
            downloadBtn.className = 'button';
            downloadBtn.textContent = 'Download';
            downloadBtn.onclick = () => window.open(img.src, '_blank');

            actions.appendChild(downloadBtn);

            content.appendChild(title);
            content.appendChild(desc);
            content.appendChild(actions);

            card.appendChild(img);
            card.appendChild(content);

            memesContainer.appendChild(card);
        });
}


