# ssnap_production_code

Code for running of SAMueL analysis by SSNAP

# Required fields

| Field name (in analysis)              | Relevant SSNAP field name | Data type    | Notes                                   |
|---------------------------------------|---------------------------|--------------|-----------------------------------------|
| stroke team                           | TeamName                  | String       |                                         |
| age                                   | S1AgeOnArrival            | Integer      |                                         |
| male                                  | S1Gender                  | Binary (0/1) | S1Gender = “M"                          |
| infarction                            | S2StrokeType              | Binary (0/1) | S2StrokeType = ‘I'                      |
| onset-to-arrival time                 | (Derived)                 | Float        | Derived onset-to-arrival time (minutes) |
| onset time known                      | S1OnsetTimeType           | Binary (0/1) | S1OnsetTimeType = “P"                   |
| precise onset known                   | S1OnsetTimeType           | Binary (0/1) | S1OnsetTimeType != ‘NK'                 |
| onset during sleep                    | S1OnsetTimeType           | Binary (0/1) | S1OnsetTimeType = “DS"                  |
| arrive by ambulance                   | S1ArriveByAmbulance       | Binary (0/1) | S1ArriveByAmbulance = ‘Y'               |
| year                                  | S1FirstArrivalDateTime    | Integer      | Extract year (e.g. 2021)                |
| anticoagulant for atrial fibrillation | S2CoMAFAnticoagulent      | Binary (0/1) | S2CoMAFAnticoagulent = ‘Y'              |
| prior disability                      | S2RankinBeforeStroke      | Integer      |                                         |
| Arrival-to-scan time                  | (Derived)                 | Integer      | Derived arrival-to-scan time (minutes)  |
| thrombolysis                          | S2Thrombolysis            | Binary (0/1) | S2Thrombolysis = ‘Y'                    |
| scan-to-thrombolysis time             | (Derived)                 | Integer      | Derived scan-to-thrombolysis time       |
| death                                 | S7DischargeType           | Binary (0/1) | S7DischargeType = ‘D'                   |
| discharge disability                  | S7RankinDischarge         | Integer      |                                         |
