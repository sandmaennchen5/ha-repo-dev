function buildUrl() {

    const label =
        encodeURIComponent(
            document.getElementById(
                "overrideLabel"
            ).value
        );

    const value =
        encodeURIComponent(
            document.getElementById(
                "overrideValue"
            ).value
        );

    const color =
        encodeURIComponent(
            document.getElementById(
                "overrideColor"
            ).value
        );

    let url =

        `https://img.shields.io/badge/` +

        `${label}-${value}-${color}`;

    const params =
        new URLSearchParams();

    const style =
        document.getElementById(
            "overrideStyle"
        ).value;

    const logo =
        document.getElementById(
            "overrideLogo"
        ).value;

    const logoColor =
        document.getElementById(
            "overrideLogoColor"
        ).value;

    if (style) {

        params.append(
            "style",
            style
        );

    }

    if (logo) {

        params.append(
            "logo",
            logo
        );

    }

    if (logoColor) {

        params.append(
            "logoColor",
            logoColor
        );

    }

    if (params.toString()) {

        url +=
            "?" +
            params.toString();

    }

    return url;

}


document.addEventListener(

    "DOMContentLoaded",

    async () => {

        if (
            !document.getElementById(
                "labApp"
            )
        ) {

            return;

        }

        const response =
            await fetch(
                BASE_URL +
                "/data/apps.json"
            );

        const apps =
            await response.json();

        const appSelect =
            document.getElementById(
                "labApp"
            );

        const badgeSelect =
            document.getElementById(
                "labBadge"
            );

        const preview =
            document.getElementById(
                "labPreview"
            );

        const url =
            document.getElementById(
                "labUrl"
            );

        const markdown =
            document.getElementById(
                "labMarkdown"
            );

        const definition =
            document.getElementById(
                "labDefinition"
            );

        const diff =
            document.getElementById(
                "labDiff"
            );

        const yaml =
            document.getElementById(
                "labYaml"
            );

        const json =
            document.getElementById(
                "labJson"
            );


        apps.forEach(

            app => {

                appSelect.innerHTML +=

                    `<option value="${app.slug}">
${app.name}
</option>`;

            }

        );


        function updateBadges() {

            badgeSelect.innerHTML =
                "";

            const app =
                apps.find(
                    x =>
                    x.slug ===
                    appSelect.value
                );

            app.badges.forEach(

                badge => {

                    badgeSelect.innerHTML +=

                        `<option value="${badge.id}">
${badge.label}
</option>`;

                }

            );

            update();

        }


        function update() {

            const app =
                apps.find(
                    x =>
                    x.slug ===
                    appSelect.value
                );

            const badge =
                app.badges.find(
                    x =>
                    x.id ===
                    badgeSelect.value
                );


            const label =
                document.getElementById(
                    "overrideLabel"
                ).value;

            const value =
                document.getElementById(
                    "overrideValue"
                ).value;

            const color =
                document.getElementById(
                    "overrideColor"
                ).value;

            const style =
                document.getElementById(
                    "overrideStyle"
                ).value;

            const logo =
                document.getElementById(
                    "overrideLogo"
                ).value;

            const logoColor =
                document.getElementById(
                    "overrideLogoColor"
                ).value;


            const badgeUrl =
                buildUrl();

            preview.src =
                badgeUrl;

            url.value =
                badgeUrl;

            markdown.value =

                `![${label}](${badgeUrl})`;

            definition.textContent =

                JSON.stringify(
                    badge,
                    null,
                    2
                );


            diff.textContent =

                JSON.stringify(

                    {

                        label,
                        value,
                        color,
                        style,
                        logo,
                        logoColor

                    },

                    null,

                    2

                );


            json.value =

                JSON.stringify(

                    {

                        label,
                        value,
                        color,
                        style,
                        logo,
                        logoColor

                    },

                    null,

                    2

                );


            yaml.value =

`label: ${label}
value: ${value}
color: ${color}
style: ${style}
logo: ${logo}
logoColor: ${logoColor}`;

        }


        appSelect.onchange =
            updateBadges;

        badgeSelect.onchange =
            update;


        [
            "overrideLabel",
            "overrideValue",
            "overrideColor",
            "overrideStyle",
            "overrideLogo",
            "overrideLogoColor"

        ].forEach(

            id => {

                document.getElementById(
                    id
                ).oninput =
                    update;

            }

        );


        document.getElementById(
            "copyUrl"
        ).onclick =
            () =>

                navigator.clipboard
                    .writeText(
                        url.value
                    );


        document.getElementById(
            "copyMarkdown"
        ).onclick =
            () =>

                navigator.clipboard
                    .writeText(
                        markdown.value
                    );


        document.getElementById(
            "copyYaml"
        ).onclick =
            () =>

                navigator.clipboard
                    .writeText(
                        yaml.value
                    );


        document.getElementById(
            "copyJson"
        ).onclick =
            () =>

                navigator.clipboard
                    .writeText(
                        json.value
                    );


        updateBadges();

    }

);