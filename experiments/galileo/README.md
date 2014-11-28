| Shield pin | Function | Linux           | Level Shifter GPIO | 22k Pull-Up GPIO | Pin Mux 1 GPIO | Pin Mux 2 GPIO | Interrupt modes |
|------------|----------|-----------------|--------------------|------------------|----------------|----------------|-----------------|
|            |          |                 | L: dir_out         | L: pulldown      |                |                | L: low-level    |
|            |          |                 | H: dir_in          | H: pullup        |                |                | H:high-level    |
|            |          |                 | I: *               | I: off           |                |                | R:rising-edge   |
|            |          |                 |                    |                  |                |                | F:falling-edge  |
|            |          |                 |                    |                  |                |                | B:both edges    |
| IO0        | UART0 RX | ttyS0           | gpio32             | gpio33           | -              | -              | -               |
|            | GPIO     | gpio11          |                    |                  | -              | -              | L/H/R/F         |
| IO1        | UART0 TX | ttyS0           | gpio28             | gpio29           | gpio45 (H)     | -              | -               |
|            | GPIO     | gpio12          |                    |                  | gpio45 (L)     | -              | L/H/R/F         |
| IO2        | UART1 RX | ttyS1           | gpio34             | gpio35           | gpio77 (H)     | -              |                 |
|            | GPIO     | gpio13          |                    |                  | gpio77 (L)     | -              | L/H/R/F         |
|            | GPIO     | gpio61          | -                  |                  | gpio77 (L)     | -              | R/F/B           |
| IO3        | UART1 TX | ttyS1           | gpio16             | gpio17           | gpio76(H)      | -              | -               |
|            | GPIO     | gpio14          |                    |                  | gpio76(L)      | gpio64(L)      | L/H/R/F         |
|            | PWM      | pwm1            |                    |                  | gpio76(L)      | gpio64(H)      | -               |
|            | GPIO     | gpio62          | -                  |                  | gpio76(L)      | gpio64(L)      | R/F/B           |
| IO4        | GPIO     | gpio6           | gpio36             | gpio37           | -              | -              | R/F/B           |
| IO5        | GPIO     | gpio0           | gpio18             | gpio19           | gpio66(L)      | -              | R/F/B           |
|            | PWM      | pwm3            |                    |                  | gpio66(H)      | -              | -               |
| IO6        | GPIO     | gpio1           | gpio20             | gpio21           | gpio68(L)      | -              | R/F/B           |
|            | PWM      | pwm5            |                    |                  | gpio68(H)      | -              | -               |
| IO7        | GPIO     | gpio38          | -                  | gpio39           | -              | -              | -               |
| IO8        | GPIO     | gpio40          | -                  | gpio41           | -              | -              | -               |
| IO9        | GPIO     | gpio4           | gpio22             | gpio23           | gpio70(L)      | -              | R/F/B           |
|            | PWM      | pwm7            |                    |                  | gpio70(L)      | -              | -               |
| IO10       | GPIO     | gpio10          | gpio26             | gpio27           | gpio74(L)      | -              | L/H/R/F         |
|            | PWM      | pwm11           |                    |                  | gpio74(H)      | -              | -               |
| IO11       | GPIO     | gpio5           | gpio24             | gpio25           | gpio44(L)      | gpio72(L)      | R/F/B           |
|            | SPI MOSI | spidev1.0       |                    |                  | gpio44(H)      | gpio72(L)      | -               |
|            | PWM      | pwm9            |                    |                  | -              | gpio72(H)      | -               |
| IO12       | GPIO     | gpio15          | gpio42             | gpio43           | -              | -              | L/H/R/F         |
|            | SPI MISO | spidev1.0       |                    |                  |                |                | -               |
| IO13       | GPIO     | gpio7           | gpio30             | gpio31           | gpio46(L)      | -              | R/F/B           |
|            | SPI SCK  | spidev1.0       |                    |                  | gpio46(H)      | -              | -               |
| IO14       | GPIO     | gpio48          | -                  | gpio49           | -              | -              | R/F/B           |
|            | ADC A0   | in_voltage0_raw |                    |                  |                |                | -               |
| IO15       | GPIO     | gpio50          | -                  | gpio51           | -              | -              | R/F/B           |
|            | ADC A1   | in_voltage1_raw |                    |                  |                |                | -               |
| IO16       | GPIO     | gpio52          | -                  | gpio53           | -              | -              | R/F/B           |
|            | ADC A2   | in_voltage2_raw |                    |                  |                |                | -               |
| IO17       | GPIO     | gpio54          | -                  | gpio55           | -              | -              | R/F/B           |
|            | ADC A3   | in_voltage3_raw |                    |                  |                |                | -               |
| IO18       | GPIO     | gpio56          | -                  | gpio57           | gpio60(H)      | gpio78(H)      | R/F/B           |
|            | ADC A4   | in_voltage4_raw |                    |                  | gpio60(H)      | gpio78(L)      | -               |
|            | I2C SDA  | i2c-0           |                    |                  | gpio60(L)      | -              | -               |
| IO19       | GPIO     | gpio58          | -                  | gpio59           | gpio60(H)      | gpio79(H)      | R/F/B           |
|            | ADC A4   | in_voltage5_raw |                    |                  | gpio60(H)      | gpio79(L)      | -               |
|            | I2C SCL  | i2c-0           |                    |                  | gpio60(L)      | -              | -               |

“L” The GPIO is configured as an output, with output level as LOW
“H” The GPIO is configured as an output, with output level as HIGH
“I” The GPIO is configured as a high-impedance input
