document.addEventListener(

    "DOMContentLoaded",

    () => {

        const theme =

            localStorage.getItem(
                "theme"
            )

            ||

            "light";


        document.body.dataset.theme =
            theme;


        const select =
            document.getElementById(
                "theme"
            );

        if (
            select
        ) {

            select.value =
                theme;

            select.addEventListener(

                "change",

                e => {

                    localStorage.setItem(

                        "theme",

                        e.target.value

                    );

                    document.body.dataset.theme =

                        e.target.value;

                }

            );

        }

    }

);