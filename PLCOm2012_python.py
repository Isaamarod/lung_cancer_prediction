import math
from typing import Union

def plcom2012 (age: int, race, education: Union [str,int], bmi: float, copd: bool, cancer_hist: bool, family_hist_lung_cancer: bool, smoking_status: bool, smoking_intensity: int, duration_smoking: int,
                      smoking_quit_time: int) -> float:
    
    #' @param age a vector of patient's age
    #' @param race categorical variable of patient's race or ethnic group (White, Black, Hispanic,
    #' Asian, American Indian, Alaskan Native, Native Hawaiian, Pacific Islander)
    #' @param education education was measured in six ordinal levels: less than high-school graduate (level 1),
    #' high-school graduate (level 2), some training after high school (level 3), some college (level 4),
    #' college graduate (level 5), and postgraduate or professional degree (level 6)
    #' @param bmi a vector of patient's body mass index, per 1 unit of increase
    #' @param copd binary variable of chronic obstructive pulmonary disease (yes as 1 or no as 0)
    #' @param cancer_hist binary variable of patient's cancer history (yes as 1 or no as 0)
    #' @param family_hist_lung_cancer binary variable of patient's family history of lung cancer (yes as 1 or no as 0)
    #' @param smoking_status binary variable of patient's smoking status (current as 1 or former as 0)
    #' @param smoking_intensity a vector of the number cigarettes patient smokes per day
    #' @param duration_smoking a vector of patient's duration of smoking, per 1-yr increase
    #' @param smoking_quit_time a vector of patient's smoking quit time, per 1-yr increase

    
  race  = race.lower()
  results = []

  if (race == "white" or race == "american indian" or race == "alaskan native" or race == 1):
    model = 0.0778868 * (age - 62) - 0.0812744 * (education - 4) - 0.0274194 * (bmi - 27) + 0.3553063 * copd + 0.4589971 * cancer_hist + 0.587185 * family_hist_lung_cancer + 0.2597431 * smoking_status - 1.822606 *  (pow((smoking_intensity/10),-1) - 0.4021541613) + 0.0317321 * (duration_smoking - 27) - 0.0308572 * (smoking_quit_time - 10) - 4.532506


  elif (race == "black" or race == 2) :
    model = 0.0778868 * (age - 62) - 0.0812744 * (education - 4) - 0.0274194 * (bmi - 27) + 0.3553063 * copd + 0.4589971 * cancer_hist + 0.587185 * family_hist_lung_cancer + 0.2597431 * smoking_status - 1.822606 * (pow((smoking_intensity/10),-1) - 0.4021541613) + 0.0317321 * (duration_smoking - 27) - 0.0308572 * (smoking_quit_time - 10) - 4.532506 + 0.3944778


  elif (race == "hispanic" or race == 3) :
    model = 0.0778868 * (age - 62) - 0.0812744 * (education - 4) - 0.0274194 * (bmi - 27) + 0.3553063 * copd + 0.4589971 * cancer_hist + 0.587185 * family_hist_lung_cancer + 0.2597431 * smoking_status - 1.822606 * (pow((smoking_intensity/10),-1) - 0.4021541613) + 0.0317321 * (duration_smoking - 27) - 0.0308572 * (smoking_quit_time - 10) - 4.532506 - 0.7434744


  elif (race == "asian" or race == 4) :
    model = 0.0778868 * (age - 62) - 0.0812744 * (education - 4) - 0.0274194 * (bmi - 27) + 0.3553063 * copd + 0.4589971 * cancer_hist + 0.587185 * family_hist_lung_cancer + 0.2597431 * smoking_status - 1.822606 * (pow((smoking_intensity/10),-1) - 0.4021541613) + 0.0317321 * (duration_smoking - 27) - 0.0308572 * (smoking_quit_time - 10) - 4.532506 - 0.466585


  elif (race == "native hawaiian" or race == "pacific islander" or race == 5) :
    model = 0.0778868 * (age - 62) - 0.0812744 * (education - 4) - 0.0274194 * (bmi - 27) + 0.3553063 * copd + 0.4589971 * cancer_hist + 0.587185 * family_hist_lung_cancer + 0.2597431 * smoking_status - 1.822606 * (pow((smoking_intensity/10),-1) - 0.4021541613) + 0.0317321 * (duration_smoking - 27) - 0.0308572 * (smoking_quit_time - 10) - 4.532506 + 1.027152


  prob = math.exp(model)/(1 + math.exp(model))
  return(prob)

  
 #plcom2012(age=62, race='black', education=4, bmi=27, copd=0, cancer_hist=0, family_hist_lung_cancer=0, smoking_status=0, smoking_intensity=80, duration_smoking=27, smoking_quit_time=10)