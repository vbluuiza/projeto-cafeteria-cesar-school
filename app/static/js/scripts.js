const radioGroup = [
  document.getElementById("radioItem1"),
  document.getElementById("radioItem2"),
  document.getElementById("radioItem3"),
  document.getElementById("radioItem4"),
  document.getElementById("radioItem5")
].filter(Boolean); // Filtra para remover possíveis elementos null/undefined

radioGroup.forEach(item => {
  item.addEventListener('click', () => {
    radioGroup.forEach(i => i.classList.remove('active'));
    item.classList.add('active');
  });
});