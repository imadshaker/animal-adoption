
    document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
    // Supprimez les messages d'erreur précédents
    clearErrorMessages();

    // Validation du nom de l'animal (entre 3 et 20 caractères)
    const nomInput = document.getElementById('nom');
    if (nomInput.value.length < 3 || nomInput.value.length > 20) {
    event.preventDefault(); // Empêche l'envoi du formulaire
    displayErrorMessage(nomInput, 'Le nom de l\'animal doit avoir entre 3 et 20 caractères.');
}

    if (!validatePostalCode()) {
        event.preventDefault(); // Empêche l'envoi du formulaire
    }
    function validatePostalCode() {
        const postalCodeInput = document.getElementById('code');
        const regex = /^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$/;
        if (!regex.test(postalCodeInput.value)) {
            displayErrorMessage(postalCodeInput, "Veuillez entrer un code postal canadien valide. Exemple: A1A 1A1.");
            return false;
        }
        return true;
    }

    // Validation de l'âge (valeur numérique entre 0 et 30)
    const ageInput = document.getElementById('age');
    const ageValue = parseFloat(ageInput.value);
    if (isNaN(ageValue) || ageValue < 0 || ageValue > 30) {
    event.preventDefault(); // Empêche l'envoi du formulaire
    displayErrorMessage(ageInput, 'L\'âge doit être une valeur numérique entre 0 et 30.');
}

    // Validation de l'adresse courriel
    const emailInput = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value)) {
    event.preventDefault(); // Empêche l'envoi du formulaire
    displayErrorMessage(emailInput, 'L\'adresse courriel doit avoir un format valide.');
}


    // Validation pour empêcher les virgules dans tous les champs
    const allInputs = document.querySelectorAll('input[type="text"]');
    allInputs.forEach(input => {
    if (input.value.includes(',')) {
    event.preventDefault(); // Empêche l'envoi du formulaire
    displayErrorMessage(input, 'Aucun champ ne peut contenir une virgule.');
    }
    });
    });

    function displayErrorMessage(input, message) {
    const errorDiv = document.createElement('div');
    errorDiv.classList.add('error-message');
    errorDiv.textContent = message;
    input.parentNode.appendChild(errorDiv);
}

    function clearErrorMessages() {
    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(errorMessage => {
    errorMessage.parentNode.removeChild(errorMessage);
});
}
});

