document.getElementById("randevutarih").addEventListener("change", async function() {
    var randevutarih = this.value;

    try {
        var response = await fetch(window.location.origin + '/randevualkaydet/', {
            method: 'POST',
            body: JSON.stringify({
                'randevutarih': randevutarih,
            }),
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        var data = await response.json();
        console.log(data);

        document.getElementById("tabloAlani").innerHTML = data.table_html;
        document.getElementById("tabloAlani").style.display = "block";

        var randevuAlButton = document.getElementById("randevuAlButton");
        if (randevuAlButton) {
            randevuAlButton.addEventListener("click", async function() {
                var checkedCheckbox = document.querySelector(".form-check-input:checked");
                if (checkedCheckbox) {
                    var row = checkedCheckbox.closest("tr");
                    var cells = row.getElementsByTagName("td");
                    var rowData = [];

                    for (var i = 0; i < cells.length - 1; i++) {
                        rowData.push(cells[i].innerText);
                    }

                    try {
                        var response = await fetch("/randevualekle/", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify({
                                "veriler": rowData,
                            }),
                        });

                        if (!response.ok) {
                            throw new Error("Network response was not ok");
                        }

                        var responseData = await response.json();
                        console.log(responseData);

                        showSuccessAlert();
                        alert('Randevu başarıyla alındı.');
                        location.reload();

                    } catch (error) {
                        console.error("There was a problem:", error);
                    }
                } else {
                    console.log("Hiçbir satır işaretli değil.");
                }
            });
        } else {
            console.error("randevuAlButton bulunamadı!");
        }

    } catch (error) {
        console.error("There was a problem:", error);
    }
});

function showSuccessAlert() {
    var alertDiv = document.getElementById("successAlert");
    if (alertDiv) {
        alertDiv.style.display = "block";
        setTimeout(function() {
            alertDiv.style.display = "none";
        }, 5000);
    }
}