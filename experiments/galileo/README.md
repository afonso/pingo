| GPIO Pins Assignment |                 |                              |                                                      |
|----------------------|-----------------|------------------------------|------------------------------------------------------|
|                      |                 |                              |                                                      |
| Quark X1000          | Sysfs GPIO #    | Signal Name / Arduino Port # | Function and Comments                                |
| GPIO_SUS0            | gpio2           | INT_N_S3                     | Don’t touch, or bad things will happen :-)           |
| GPIO_SUS1            | gpio3           | GP LED                       | LED between Cypress CY8C9540A and RTC battery header |
| GPIO_SUS2            | gpio4           | LVL_OE                       | TXS0108E level shifter output enable.                |
| GPIO_SUS3            | gpio5           | GPIO_SUS3_PCIE_RESET_N       | Reset to Mini PCI-E slot                             |
| GPIO_SUS4            | gpio6           | GPIO_SUS4_W_DISABLE_N        | Wireless disable (RF Kill to PCI-E Slot)             |
| GPIO_SUS5            | gpio7           | A0_N                         | Jumper J2 (Cypress CY8C9540A I2C address select)     |
| GPIO0                | gpio8           | SPI0_CS_N                    | Select SPI for AD7298                                |
| GPIO1                | gpio9           | Not Connected                |                                                      |
| GPIO2                | gpio10          | SPI1_CS_N                    | Routed to IO10 if selected by IO10_MUX (libgpio42=0) |
| GPIO3                | gpio11          | Not Connected                |                                                      |
| GPIO4                | gpio12          | XRES                         | Reset to Cypress CY8C9540A                           |
| GPIO5                | gpio13          | INT_N_S0                     | Don’t touch too :-)                                  |
| GPIO6                | gpio14          | IO2                          | Selected by IO2_MUX (gpio31=0)                       |
| GPIO7                | gpio15          | IO3                          | Selected by IO3_MUX (gpio30=0)                       |
| GPIO8                | gpio0           | GLN_IO2_PU_EN                | Enable pullup on IO2/GPIO6                           |
| GPIO9                | gpio1           | GLN_IO3_PU_EN                | Enable pullup on IO3/GPIO7                           |
| CY8C9540A            | Sysfs GPIO #    | Signal Name / Arduino Port # | Function and Comments                                |
| GPORT0_BIT0          | gpio16          | IO10                         | Selected by IO10_MUX (GPORT3_BIT6, gpio42)           |
|                      |                 |                              | Also controlled by pwm7                              |
| GPORT0_BIT1          | gpio17          | IO5                          | Also controlled by pwm5                              |
| GPORT0_BIT2          | gpio18          | IO3                          | Selected by IO3_MUX (gpio30=1)                       |
|                      |                 |                              | Also controlled by pwm3                              |
| GPORT0_BIT3          | gpio19          | IO9                          | Also controlled by pwm1                              |
| GPORT0_BIT4          | gpio20          | A5_MUX                       | Selects A5 pin routing:                              |
|                      |                 |                              | 0 = AD7298 (VIN5)                                    |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT5, gpio49)          |
| GPORT0_BIT5          | gpio21          | A4_MUX                       | Selects A4 pin routing:                              |
|                      |                 |                              | 0 = AD7298 (VIN4)                                    |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT4, gpio48)          |
| GPORT0_BIT6          | gpio22          | A3_MUX                       | Selects A3 pin routing:                              |
|                      |                 |                              | 0 = AD7298 (VIN3)                                    |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT3, gpio47)          |
| GPORT0_BIT7          | gpio23          | A2_MUX                       | Selects A2 pin routing:                              |
|                      |                 |                              | 0 = AD7298 (VIN2)                                    |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT2, gpio46)          |
| GPORT1_BIT0          | gpio24          | IO6                          | Also controlled by pwm6                              |
| GPORT1_BIT1          | gpio25          | IO11                         | Selected by IO11_MUX (GPORT3_BIT7, gpio43)           |
|                      |                 |                              | Also controlled by pwm4                              |
| GPORT1_BIT2          | gpio26          | IO8                          |                                                      |
| GPORT1_BIT3          | gpio27          | IO7                          |                                                      |
| GPORT1_BIT4          | gpio28          | IO4                          |                                                      |
| GPORT1_BIT5          | gpio29          | I2C_MUX                      | Selects between GPIO and I2C on pins A4 and A5:      |
|                      |                 |                              | 0= Quark I2C                                         |
|                      |                 |                              | 1 = GPIO (Cypress CY8C9540A, AD7298)                 |
| GPORT1_BIT6          | gpio30          | IO3_MUX                      | Selects IO3 pin routing:                             |
|                      |                 |                              | 0 = Quark (GPIO7, gpio15)                            |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT9_BIT2, gpio18)          |
| GPORT1_BIT7          | gpio31          | IO2_MUX                      | Selects IO2 pin routing:                             |
|                      |                 |                              | 0 = Quark (GPIO6, gpio14)                            |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT2_BIT0, gpio32)          |
| GPORT2_BIT0          | gpio32          | IO2                          | Selected by IO_MUX (gpio31=1)                        |
| GPORT2_BIT1          | gpio33          | Not Connected                |                                                      |
| GPORT2_BIT2          | gpio34          | Not Connected                |                                                      |
| GPORT2_BIT3          | gpio35          | Not Connected                |                                                      |
| GPORT3_BIT0          | gpio36          | A1_MUX                       | Select A1 pin routing:                               |
|                      |                 |                              | 0 = AD7298 (VIN1)                                    |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT1, gpio45)          |
| GPORT3_BIT1          | gpio37          | A0_MUX                       | Select A0 pin routing:                               |
|                      |                 |                              | 0 = AD7298 (VIN0)                                    |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT0, gpio44)          |
| GPORT3_BIT2          | gpio38          | IO12                         | Selected by IO12_MUX (gpio54=1)                      |
| GPORT3_BIT3          | gpio39          | IO13                         | Selected by IO13_MUX (gpio55=1)                      |
| GPORT3_BIT4          | gpio40          | IO0_MUX                      | Select IO0 pin routing:                              |
|                      |                 |                              | 0 = Quark UART0 RXD (/dev/ttyS0)                     |
|                      |                 |                              | 1 = Cypress CY8C9540A (GPORT4_BIT6, gpio50)          |
| GPORT3_BIT5          | gpio41          | IO1_MUX                      | Select IO1 pin routing:                              |
|                      |                 |                              | 0 = Quark UART0 TXD (/dev/ttyS0)                     |
|                      |                 |                              | 1 = Cypress (GPORT4_BIT7, gpio51)                    |
| GPORT3_BIT6          | gpio42          | IO10_MUX                     | Select IO10 pin routing:                             |
|                      |                 |                              | 0 = Quark SPI1_CS                                    |
|                      |                 |                              | 1 = Cypress (GPORT0_BIT0, gpio16)                    |
| GPORT3_BIT7          | gpio43          | IO11_MUX                     | Select IO11 pin routing:                             |
|                      |                 |                              | 0 = Quark SPI1_MOSI                                  |
|                      |                 |                              | 1 = Cypress (GPORT1_BIT1, gpio25)                    |
| GPORT4_BIT0          | gpio44          | A0                           | Selected by A0_MUX (gpio37=1)                        |
| GPORT4_BIT1          | gpio45          | A1                           | Selected by A1_MUX (gpio36=1)                        |
| GPORT4_BIT2          | gpio46          | A2                           | Selected by A2_MUX (gpio23=1)                        |
| GPORT4_BIT3          | gpio47          | A3                           | Selected by A3_MUX (gpio22=1)                        |
| GPORT4_BIT4          | gpio48          | A4                           | Selected by A4_MUX (gpio21=1) and I2C_MUX (gpio29=1) |
| GPORT4_BIT5          | gpio49          | A5                           | Selected by A5_MUX (gpio20=1) and I2C_MUX (gpio29=1) |
| GPORT4_BIT6          | gpio50          | IO0                          | Selected by IO0_MUX (gpio40=1)                       |
| GPORT4_BIT7          | gpio51          | IO1                          | Selected by IO1_MUX (gpio41=1)                       |
| GPORT5_BIT0          | gpio52          | RESET (Input)                | Connected to shield and to the RESET button.         |
| GPORT5_BIT1          | gpio53          | RESET (Output)               |                                                      |
| GPORT5_BIT2          | gpio54          | IO12_MUX                     | Selects IO12 pin routing:                            |
|                      |                 |                              | 0 = Quark SPI_MISO                                   |
|                      |                 |                              | 1 = Cypress (PORT3_BIT2, gpio38)                     |
| GPORT5_BIT3          | gpio55          | IO13_MUX                     | Selects IO13 pin routing:                            |
|                      |                 |                              | 0 = Quark SPI_SCK                                    |
|                      |                 |                              | 1 = Cypress (PORT3_BIT3, gpio39)                     |
| AD7298               | Sysfs GPIO #    | Signal Name / Arduino Port # | Function and Comments                                |
| VIN1                 | in_voltage0_raw | A0                           | Selected by A0_MUX (gpio37=0)                        |
| VIN2                 | in_voltage1_raw | A1                           | Selected by A1_MUX (gpio36=0)                        |
| VIN3                 | in_voltage2_raw | A2                           | Selected by A2_MUX (gpio23=0)                        |
| VIN3                 | in_voltage3_raw | A3                           | Selected by A3_MUX (gpio22=0)                        |
| VIN4                 | in_voltage4_raw | A4                           | Selected by A4_MUX (gpio21=0) and I2C_MUX (gpio29=1) |
| VIN5                 | in_voltage5_raw | A5                           | Selected by A5_MUX (gpio20=0) and I2C_MUX (gpio29=1) |
| VIN6                 | in_voltage6_raw | Not Connected                |                                                      |
| VIN7                 | in_voltage7_raw | Not Connected                |                                                      |
