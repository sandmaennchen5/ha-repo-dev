document.addEventListener(

    "DOMContentLoaded",

    () => {

        const table =
            document.getElementById(
                "matrixTable"
            );

        if (!table) {

            return;

        }

        /*
         * Search
         */

        const search =
            document.getElementById(
                "matrixSearch"
            );

        search?.addEventListener(

            "input",

            () => {

                const filter =
                    search.value
                    .toLowerCase();

                table
                    .querySelectorAll(
                        "tbody tr"
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

        /*
         * Sort by Name
         */

        const sortByName =
            document.getElementById(
                "sortByName"
            );

        sortByName?.addEventListener(

            "click",

            () => {

                const tbody =
                    table.querySelector(
                        "tbody"
                    );

                const rows =
                    Array.from(
                        tbody.rows
                    );

                rows.sort(

                    (a, b) =>

                        a.cells[0]
                            .innerText
                            .localeCompare(
                                b.cells[0]
                                    .innerText
                            )

                );

                rows.forEach(

                    row =>
                        tbody.appendChild(
                            row
                        )

                );

            }

        );

        /*
         * Sort by Score
         */

        const sortByScore =
            document.getElementById(
                "sortByScore"
            );

        sortByScore?.addEventListener(

            "click",

            () => {

                const tbody =
                    table.querySelector(
                        "tbody"
                    );

                const rows =
                    Array.from(
                        tbody.rows
                    );

                rows.sort(

                    (a, b) =>

                        Number(
                            b.dataset.score || 0
                        )

                        -

                        Number(
                            a.dataset.score || 0
                        )

                );

                rows.forEach(

                    row =>
                        tbody.appendChild(
                            row
                        )

                );

            }

        );

        /*
         * Hide Empty Columns
         */

        const hideEmpty =
            document.getElementById(
                "hideEmpty"
            );

        function updateEmptyColumns() {

            const rows =
                Array.from(
                    table.rows
                );

            if (
                rows.length === 0
            ) {

                return;

            }

            const cols =
                rows[0].cells.length;

            for (
                let c = 1;
                c < cols;
                c++
            ) {

                let hasValue =
                    false;

                for (
                    let r = 1;
                    r < rows.length;
                    r++
                ) {

                    if (
                        rows[r]
                            .cells[c]
                            ?.querySelector(
                                "img"
                            )
                    ) {

                        hasValue =
                            true;

                        break;

                    }

                }

                const display =

                    hideEmpty?.checked &&
                    !hasValue

                    ? "none"
                    : "";

                rows.forEach(

                    row => {

                        if (
                            row.cells[c]
                        ) {

                            row.cells[c]
                                .style.display =
                                display;

                        }

                    }

                );

            }

        }

        hideEmpty?.addEventListener(
            "change",
            updateEmptyColumns
        );

        updateEmptyColumns();

        /*
         * CSV Export
         */

        const exportCsv =
            document.getElementById(
                "exportCsv"
            );

        exportCsv?.addEventListener(

            "click",

            () => {

                let csv = "";

                Array.from(
                    table.rows
                ).forEach(

                    row => {

                        const values =

                            Array.from(
                                row.cells
                            ).map(

                                cell => {

                                    const text =
                                        cell.innerText
                                            .trim();

                                    if (
                                        text
                                    ) {

                                        return text;

                                    }

                                    return cell.querySelector(
                                        "img"
                                    )
                                        ? "✓"
                                        : "";

                                }

                            );

                        csv +=

                            values.join(
                                ";"
                            )

                            + "\n";

                    }

                );

                const blob =
                    new Blob(
                        [csv],
                        {
                            type:
                                "text/csv"
                        }
                    );

                const link =
                    document.createElement(
                        "a"
                    );

                link.href =
                    URL.createObjectURL(
                        blob
                    );

                link.download =
                    "matrix.csv";

                link.click();

            }

        );

        /*
         * Markdown Export
         */

        const exportMarkdown =
            document.getElementById(
                "exportMarkdown"
            );

        exportMarkdown?.addEventListener(

            "click",

            async () => {

                let md = "";

                Array.from(
                    table.rows
                ).forEach(

                    (
                        row,
                        index
                    ) => {

                        const values =

                            Array.from(
                                row.cells
                            ).map(

                                cell => {

                                    const text =
                                        cell.innerText
                                            .trim();

                                    if (
                                        text
                                    ) {

                                        return text;

                                    }

                                    return cell.querySelector(
                                        "img"
                                    )
                                        ? "✓"
                                        : "";

                                }

                            );

                        md +=
                            "| " +
                            values.join(
                                " | "
                            ) +
                            " |\n";

                        if (
                            index === 0
                        ) {

                            md +=
                                "| " +
                                values
                                    .map(
                                        () =>
                                            "---"
                                    )
                                    .join(
                                        " | "
                                    ) +
                                " |\n";

                        }

                    }

                );

                await navigator
                    .clipboard
                    .writeText(
                        md
                    );

                alert(
                    "Markdown copied to clipboard"
                );

            }

        );

    }

);