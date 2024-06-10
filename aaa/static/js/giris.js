document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    var username = document.querySelector("#login-form.txt").value;
    var password = document.querySelectorAll("#login-form.txt")[1].value;
    var userType = document.getElementById("user-type").value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/test/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.open("POST", "/patient_signup/", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    // Başarılı giriş

                    console.log(response.message);
                } else {
                    // Başarısız giriş
                    console.error(response.message);
                }
            } else {
                // Hata
                console.error("Hata kodu: " + xhr.status);
            }
        }
    };

    var data = JSON.stringify({
        username: username,
        password: password,
        userType: userType
    });

    var url = "";
    if (userType === "doctor") {
        url = "/doctor-login/";
    } else if (userType === "patient") {
        url = "/patient-login/";
    } else if (userType === "admin") {
        url = "/admin-login/";
    }

    xhr.send(data);
});


document.getElementById("signup-link").addEventListener("click", function(event) {
    event.preventDefault();
    var userType = document.getElementById("user-type").value;

    if (userType === "doctor") {
        document.getElementById("login-form").style.display = "none"; //Giriş formunu gizle
        document.getElementById("doctor-signup-form").style.display = "block"; //Doktor kayıt formunu göster
    } else if (userType === "patient") {
        document.getElementById("login-form").style.display = "none"; //Giriş formunu gizle
        document.getElementById("patient-signup-form").style.display = "block"; //Hasta kayıt formunu göster
    } else {
        console.error("Geçersiz kullanıcı türü.");
    }
});
document.getElementById("login-button").addEventListener("click", async function(event) {
    event.preventDefault();
    var userType = document.getElementById("user-type").value;
    console.log('Hello World');
    var username = document.getElementById("username").value;
    console.log(username);
    var lastname = document.getElementById("last-name").value;
    console.log(lastname);
    var password = document.getElementById("password").value;
    console.log(password);
   try {

       if((userType) == "patient") {
           var response = await fetch(window.location.origin + '/test/', {
               method: 'POST',
               body: JSON.stringify({
                   //stringfy javascript nesnesini json formatına donusturur wievs den yakalarız
                   'username': username,
                   'last-name': lastname,
                   'password': password,
               }),
               headers: {
                   'Content-type': 'application/json',
               }
           });

           if (!response.ok) {
               throw new Error("Network response was not ok");
           }

           var data = await response.json();
           console.log(data.message);

           var gelen;
           if (data['flg'] === 1) {
               console.log("Thats it resu and girissss");
               window.location.href = "/patient_login"; //Django URLsine göre yönlendirme yapılacak
           }

           if (data['resu'] == 200) {
               console.log("Thats it resu");
           } else if (data['resu'] == 404) {
               console.log("thats it is false resu");
           }
       }
       else if((userType) == "doctor")
       {
           var response = await fetch(window.location.origin + '/doctor_login/', {
               method: 'POST',
               body: JSON.stringify({
                   //stringfy javascript nesnesini json formatına donusturur wievs den yakalarız
                   'username': username,
                   'last-name': lastname,
                   'password': password,
               }),
               headers: {
                   'Content-type': 'application/json',
               }
           });
           if (!response.ok) {
               throw new Error("Network response was not ok");
           }

           var data = await response.json();
           console.log(data.message);

           var gelen;
           if (data['flg'] === 1) {
               console.log("Thats it resu and doktor girissss");
               window.location.href = "/doctor_loginview"; //Django URLsine göre yönlendirme yapılacak
           }

           if (data['resu'] == 200) {
               console.log("Thats it resu");
           } else if (data['resu'] == 404) {
               console.log("thats it is false resu");
           }

       }
    } catch (error) {
        console.error("There was a problem:", error);
    }

    document.getElementById("username").innerText = username;
});

//HASTA KAYIT EKRANI
document.getElementById("patient-signup-button").addEventListener("click", async function(event){
    event.preventDefault();
    var name = document.getElementById("name").value;
    console.log(name);
    var lastname = document.getElementById("lastname").value;
    console.log(lastname);
    var gender = document.getElementById("gender").value;
    console.log(gender);
    var date = document.getElementById("date").value;
    console.log(date);
    var phone_no = document.getElementById("phone_no").value;
    console.log(phone_no);
    var address = document.getElementById("address").value;
    console.log(address);
    var password = document.getElementById("sign-up-password").value;
    console.log(password);

    try {
        var response = await fetch(window.location.origin + '/patient-signup/',{
            method: 'POST',
            body: JSON.stringify({
                //stringfy javascript nesnesini json formatına donusturur views den yakalarız
                'name': name,
                'lastname': lastname,
                'gender': gender,
                'date': date,
                'phone_no': phone_no,
                'address': address,
                'password': password,
            }),
            headers: {
                'Content-type': 'application/json',
            }
        });

        if (!response.ok)
            throw new Error("Network response was not ok");

        var data = await response.json();
        console.log(data.message);

        if (data['resu'] == 200)
            console.log("Thats it resu");

        else if (data['resu'] == 404)
            console.log("thats it is false resu");

    }
    catch (error){
        console.error("There was a problem:", error);
    }

    document.getElementById("patient-signup-form").style.display = "none";
    document.getElementById("login-form").style.display = "block";
});

//DOKTOR KAYIT EKRANI
document.getElementById("doctor-signup-button").addEventListener("click", async function(event){
    event.preventDefault();
    var doctor_name = document.getElementById("doctor_name").value;
    console.log(doctor_name);
    var doctor_lastname = document.getElementById("doctor_lastname").value;
    console.log(doctor_lastname);
    var doctor_major = document.getElementById("doctor_major").value;
    console.log(doctor_major);
    var doctor_hospital = document.getElementById("doctor_hospital").value;
    console.log(doctor_hospital);
    var doctor_signup_password = document.getElementById("doctor_signup_password").value;
    console.log(doctor_signup_password);

    try {
        var response = await fetch(window.location.origin + '/doctor-signup/',{
            method: 'POST',
            body: JSON.stringify({
                //stringfy javascript nesnesini json formatına donusturur views den yakalarız
                'doctor_name': doctor_name,
                'doctor_lastname': doctor_lastname,
                'doctor_major': doctor_major,
                'doctor_hospital': doctor_hospital,
                'doctor_signup_password': doctor_signup_password,
            }),
            headers: {
                'Content-type': 'application/json',
            }
        });

        if (!response.ok)
            throw new Error("Network response was not ok");

        var data = await response.json();
        console.log(data.message);

        if (data['resu'] == 200)
            console.log("Thats it resu");

        else if (data['resu'] == 404)
            console.log("thats it is false resu");

    }
    catch (error){
        console.error("There was a problem:", error);
    }

    document.getElementById("doctor-signup-form").style.display = "none"; //Hasta kayıt formunu göster
    document.getElementById("login-form").style.display = "block"; //Giriş formunu gizle
});

function toggleMenu() {
    var menu = document.querySelector('.menu');
    menu.classList.toggle('open');
}

