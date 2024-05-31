<?php

class Lasagna
{
    public function expectedCookTime()
    {
       return 40; // Implement the expectedCookTime method
    }

    public function remainingCookTime($elapsed_minutes)
    {
        $expectedTime = $this->expectedCookTime();
        return $expectedTime - $elapsed_minutes;// Implement the remainingCookTime method
    }

    public function totalPreparationTime($layers_to_prep)
    {
     $timePerLayer = 2;
     return $layers_to_prep * $timePerLayer;// Implement the totalPreparationTime method
    }

    public function totalElapsedTime($layers_to_prep, $elapsed_minutes)
    {
        $prepTime = $this->totalPreparationTime($layers_to_prep);
        return $prepTime + $elapsed_minutes;
        // Implement the totalElapsedTime method
    }

    public function alarm()
    {
        return "Ding!";
        // Implement the alarm method
    }
}
