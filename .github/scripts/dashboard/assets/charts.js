document.addEventListener(

    "DOMContentLoaded",

    () => {

        /*
         * History Chart
         */

        if (
            typeof historyData !==
            "undefined"
        ) {

            const labels =
                historyData.map(
                    x => x.timestamp
                );

            const values =
                historyData.map(
                    x => x.apps
                );

            const canvas =
                document.getElementById(
                    "historyChart"
                );

            if (
                canvas
            ) {

                new Chart(

                    canvas,

                    {

                        type: "line",

                        data: {

                            labels,

                            datasets: [

                                {

                                    label:
                                        "Apps",

                                    data:
                                        values,

                                    tension:
                                        .3

                                }

                            ]

                        },

                        options: {

                            responsive:
                                true,

                            maintainAspectRatio:
                                false

                        }

                    }

                );

            }

        }


        /*
         * Health Chart
         */

        if (
            typeof healthStats !==
            "undefined"
        ) {

            const canvas =
                document.getElementById(
                    "healthChart"
                );

            if (
                canvas
            ) {

                new Chart(

                    canvas,

                    {

                        type:
                            "doughnut",

                        data: {

                            labels: [

                                "Green",
                                "Yellow",
                                "Red"

                            ],

                            datasets: [

                                {

                                    data: [

                                        healthStats.green,

                                        healthStats.yellow,

                                        healthStats.red

                                    ]

                                }

                            ]

                        }

                    }

                );

            }

        }

    }

);