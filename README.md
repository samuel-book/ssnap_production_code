# ssnap_production_code

Code for running of SAMueL analysis by SSNAP

## Required fields

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
| arrival-to-scan time                  | (Derived)                 | Integer      | Derived arrival-to-scan time (minutes)  |
| thrombolysis                          | S2Thrombolysis            | Binary (0/1) | S2Thrombolysis = ‘Y'                    |
| scan-to-thrombolysis time             | (Derived)                 | Integer      | Derived scan-to-thrombolysis time       |
| death                                 | S7DischargeType           | Binary (0/1) | S7DischargeType = ‘D'                   |
| discharge disability                  | S7RankinDischarge         | Integer      |                                         |


## Code structure

Code structure given as:

* package
    * module
        * Class

* samuel
    * samuel: The samuel module is the main coordinating module.
        * `Samuel`: Co-ordinates the analysis and reporting of the SSNAP data.
        
* globvars
    * globvars: The globvars module holds global variables.
        * `Globvars`: Holds global variables. They may be modified on initiation.

* general_analysis
    * descriptive_stats: Descriptive stats for each stroke team
        * `Descriptive_stats`: Performs describtive statistics for each stroke team.
        
* outcome
    * clinical_outcome: Clinical outcome (mRS and utility-weighted mRS) based on time to treatment
        * (No classes started)
    * health_economics: Helath economics model (cost6 per QAlY for changes)
        * (No classes started)
    * life_expectancy: Life expectancy model
        * (No classes started)

* output
    * output: Holds model outputs prior to preparation of report
        * `Output`: Is a container to hold model outputs
        * `Report`: Proares a LaTeX/PDF report based on results held in `Outputs`

* pathway_sim:
    * (module not yet started)
        * (No classes started)

* xgbmodel
    * xbg_thrombolysis_model: Performs explainable machine learning for prediction of thrombolysis use, based on XGBoost and SHAP.
        * `XGBThrombolysisModel`: XGBoost mode to predict use of thrombolysis
    * xbg_outcome_model: Performs explainable machine learning for prediction of clinical outcome, based on XGBoost and SHAP.
        * `XGBOutcomeModel`: XGBoost mode to predict clinical outcome
        
