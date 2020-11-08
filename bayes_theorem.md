This is a synthesis of what is Bayes theorem and how it works, using a simple example. I recommend checking 3blue1brow's video about it, as I am going to use the example he uses in it.

There's a description of a person, it sais the person is really introvert and likes living in the world of imagination. Is this person a librarian or a farmer?
Well, seeing the video and the way I explained, I am very inclined to say that you tought the person is a librarian.

The Bayes Theorem will be used to calculate the certainty you have, or the probability that you are right; as this is the use of the theorem, it gives you the probalility of a theory (the person
is a librarian) to be right, given some evidence. What is the evidence? The number of librarians and no librarians that fix in the description.

Let's assume that for every 21 people in our sample, 20 are farmers and 1 is a librarian (what gives you a propotion of 20:1). Using a items aproach to complete the formula:

P(H|E) =  P(H).P(E|H)                     P(H)P(E|H)
         -------------   ------>   -------------------------
             P(E)                  P(H)P(E|H) + P(-H)P(E|-H)

I - let's get P(H):

P(H) is the probability of, from our sample, you randomly choose librarian. Seeing that for every 21 people, one is a librarian, our P(H) is 1 / 21.

II - getting P(H|E):

P(H|E) is the probability that, from our P(H), you will randomly choose a librarian that fix in the description given. Let's say it is 4 / 10 (four for every ten)

III - getting P(H)P(E|H):

This will be the simple multiplication of P(H) and P(H|E). 1 / 21 . 4 / 10 = 4 / 210. This means that for every 210 people in our sample of farmers and librarians, 4 are librarians
that fix with the description, in other words, it's the probabiliy of the hipotesys to be true, given the evidence. This is not the certainty you can have.

IV - getting P(-H):

This can be understood as the probability of non-H, as our P(H) is the probability of a random person to be a librarian, P(-H) will be the probability of one person of being a non-librarian,
in our case, a farmer. As 1 every 21 people is a librarian, 20 of every 21 people is a non-librarian, farmer.

V - getting P(E|-H):

This is the probability of a farmer to fix in the description. Let's say it is 1 / 10 (one for every ten). We will get P(-H).P(E|-H) in the next step.

VI - doing some calculation:

using the formula, and saying that there are 210 people in our sample:

                4 / 210 . 210                           4            1
----------------------------------------------  ---> -------- ---> -----
 (4 / 210 . 210) + ((20 / 21 . 1 / 10) . 210)         4 + 20         6

so, if you sad that the person of the description is a librarian, you have 1 / 6 of certainty, given the number of librarians and no librarians that fixed in the description.
