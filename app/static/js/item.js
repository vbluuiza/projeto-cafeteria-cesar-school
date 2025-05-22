document.addEventListener('DOMContentLoaded', () => {
  const cardData = JSON.parse(localStorage.getItem('selectedCard'));

  if (cardData) {
    document.getElementById('detail-title').textContent = cardData.title;
    document.getElementById('detail-description').textContent = cardData.description;
    document.getElementById('detail-price').textContent = cardData.price;
    document.getElementById('detail-image').src = cardData.imageSrc;
  }
});