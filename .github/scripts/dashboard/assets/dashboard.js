document.addEventListener(

    "DOMContentLoaded",

    () => {

        /*
         * Dashboard Search
         */

        const search =
            document.getElementById(
                "search"
            );

        if (
            search
        ) {

            search.addEventListener(

                "input",

                () => {

                    const filter =

                        search.value
                        .toLowerCase();

                    document
                        .querySelectorAll(
                            "#appsTable tbody tr"
                        )

                        .forEach(

                            row => {

                                row.style.display =

                                    row.innerText
                                        .toLowerCase()
                                        .includes(
                                            filter
                                        )

                                    ? ""

                                    : "none";

                            }

                        );

                }

            );

        }

    }

);