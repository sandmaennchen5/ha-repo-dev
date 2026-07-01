function getFavorites() {

    return JSON.parse(

        localStorage.getItem(
            "favorites"
        )

        ||

        "[]"

    );

}


function saveFavorites(
    favorites
) {

    localStorage.setItem(

        "favorites",

        JSON.stringify(
            favorites
        )

    );

}


function toggleFavorite(
    slug
) {

    let favorites =
        getFavorites();

    if (
        favorites.includes(
            slug
        )
    ) {

        favorites =

            favorites.filter(
                x =>
                x !== slug
            );

    }

    else {

        favorites.push(
            slug
        );

    }

    saveFavorites(
        favorites
    );

}


function isFavorite(
    slug
) {

    return getFavorites()
        .includes(
            slug
        );

}


document.addEventListener(

    "DOMContentLoaded",

    () => {

        document
            .querySelectorAll(
                ".favorite-btn"
            )
            .forEach(

                button => {

                    const slug =
                        button.dataset.slug;

                    function update() {

                        button.textContent =

                            isFavorite(
                                slug
                            )

                            ? "★"

                            : "☆";

                    }

                    update();

                    button.addEventListener(

                        "click",

                        () => {

                            toggleFavorite(
                                slug
                            );

                            update();

                        }

                    );

                }

            );

    }

);