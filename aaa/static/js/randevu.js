document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.randevuSilButton').forEach(function(button) {
        button.addEventListener('click', function() {
            var row = this.closest('tr');
            var randevuID = row.querySelector('td:nth-child(2)').textContent.trim();
            console.log("Randevu ID:", randevuID);
            console.log("Butona bastım");
            randevuSil(randevuID);
        });
    });
});



function randevuSil(randevuID) {
    fetch('/randevu-iptal/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ randevuID: randevuID })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Randevu başarıyla iptal edildi.');
            location.reload();
        } else {
            alert('Randevu iptal edilemedi.');
        }
    })
    .catch(error => {
        console.error('Hata:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
