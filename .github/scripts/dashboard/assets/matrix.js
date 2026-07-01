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

        let sortState = {};

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

        const sortableHeaders =
            table.querySelectorAll(
                "th.sortable"
            );

        sortableHeaders.forEach(
            header => {
                header.style.cursor =
                    "pointer";

                header.addEventListener(
                    "click",
                    () => {
                        const columnIndex =
                            parseInt(
                                header.dataset
                                    .column
                            );

                        const isAscending =
                            sortState[columnIndex]
                            === "asc";

                        const direction =
                            isAscending
                            ? "desc"
                            : "asc";

                        sortTable(
                            columnIndex,
                            direction
                        );

                        sortState = {};
                        sortState[columnIndex] =
                            direction;

                        updateSortIndicators();
                    }
                );
            }
        );

        function sortTable(
            columnIndex,
            direction
        ) {
            const tbody =
                table.querySelector(
                    "tbody"
                );

            const rows =
                Array.from(
                    tbody.rows
                );

            rows.sort(
                (a, b) => {
                    const aVal =
                        a.cells[columnIndex]
                        ?.innerText
                        .trim() || "";

                    const bVal =
                        b.cells[columnIndex]
                        ?.innerText
                        .trim() || "";

                    const comparison =
                        aVal.localeCompare(
                            bVal,
                            undefined,
                            {
                                numeric: true
                            }
                        );

                    return direction === "asc"
                        ? comparison
                        : -comparison;
                }
            );

            rows.forEach(
                row =>
                    tbody.appendChild(
                        row
                    )
            );
        }

        function updateSortIndicators() {
            sortableHeaders.forEach(
                header => {
                    const columnIndex =
                        parseInt(
                            header.dataset
                            .column
                        );

                    const direction =
                        sortState[columnIndex];

                    header.style.color =
                        direction
                        ? "#0066cc"
                        : "inherit";

                    header.title =
                        direction
                        ? `Sortiert ${direction}`
                        : "Klicken zum Sortieren";
                }
            );
        }

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
                    "Markdown in die Zwischenablage kopiert"
                );
            }
        );
    }
);
