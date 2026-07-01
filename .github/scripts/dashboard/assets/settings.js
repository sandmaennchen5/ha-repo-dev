document.addEventListener(

    "DOMContentLoaded",

    () => {

        if (
            !localStorage.getItem(
                "theme"
            )
        ) {

            localStorage.setItem(

                "theme",

                "light"

            );

        }


        if (
            !localStorage.getItem(
                "favorites"
            )
        ) {

            localStorage.setItem(

                "favorites",

                "[]"

            );

        }

        const themeSelect =
            document.getElementById(
                "theme"
            );

        if (
            themeSelect
        ) {

            themeSelect.value =

                localStorage.getItem(
                    "theme"
                )

                ||

                "light";

            themeSelect.addEventListener(

                "change",

                () => {

                    localStorage.setItem(

                        "theme",

                        themeSelect.value

                    );

                    applyTheme();

                }

            );

        }

        applyTheme();

    }

);


function applyTheme() {

    const theme =

        localStorage.getItem(
            "theme"
        )

        ||

        "light";

    document.body.classList.remove(

        "theme-light",
        "theme-dark"

    );

    document.body.classList.add(

        "theme-" + theme

    );

}