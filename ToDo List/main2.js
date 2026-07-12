window.addEventListener("load", () => {
    const form = document.querySelector("#new-form");
    const input1 = document.querySelector("#new-input1");
    const input2 = document.querySelector("#new-input2");

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const num1 = input1.value;
        const num2 = input2.value;

        if(!num1 || !num2){
            alert("Please enter a number");
            return;
        }

        const h2_el = document.getElementById("answer");
        let ans = num1 + num2;
        h2_el.innerHTML =   ans;
    })
})