<?php

class PizzaPi
{
    public function calculateDoughRequirement($pizzas,$persons)
    {
        $dough_per_pizza = $persons*20+200;
        $dough_required =  $pizzas*($persons*20+200);
        return $dough_required;
    }

    public function calculateSauceRequirement($pizzas,$sauce_can_volume)
    {
        $sauce_per_pizza = 125;
        $total_sauce = $pizzas*$sauce_per_pizza;
        $cans_of_sauce =  $total_sauce/$sauce_can_volume;
        return $cans_of_sauce;
    }

    public function calculateCheeseCubeCoverage($cheese_dimension,$thickness,$diameter)
    {
       $cheese_per_pizza = $thickness * pi() * $diameter ;
        $no_of_pizzas = floor(pow($cheese_dimension,3)/$cheese_per_pizza);
        return  $no_of_pizzas;
            
    }
    public function calculateLeftOverSlices($no_of_pizzas,$no_of_friends)
    {
       $left_over_slices = $no_of_pizzas*8 % $no_of_friends;
        return $left_over_slices;
    }
}
