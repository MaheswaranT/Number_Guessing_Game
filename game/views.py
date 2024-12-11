from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def playground(request):
    if 'number_to_guess' not in request.session:
        request.session['number_to_guess'] = random.randint(1, 100)
        request.session['chances'] = 7
        request.session['guess_counter'] = 0

    number_to_guess = request.session['number_to_guess']
    chances = request.session['chances']
    guess_counter = request.session['guess_counter']

    guess = request.GET.get('guess')
    result = ""

    if guess:
        my_guess = int(guess)
        guess_counter += 1
        request.session['guess_counter'] = guess_counter

        if my_guess == number_to_guess:
            result = f"Congratulations! You guessed the number {number_to_guess} in {guess_counter} attempts!"
            request.session.flush()
        elif guess_counter >= chances:
            result = f"Sorry, you've used all your chances. The number was {number_to_guess}. Better luck next time!"
            request.session.flush()
        elif my_guess > number_to_guess:
            result = "Your guess is too high!"
        elif my_guess < number_to_guess:
            result = "Your guess is too low!"

    return render(request, 'playground.html', {
        'result': result,
        'chances': chances - guess_counter,
    })