final_failed_tutorials = read.csv('final_failed_tutorials.csv')
final_cut_tutorials = read.csv('final_cut_tutorials.csv')
final_tutor_amount = read.csv('final_tutor_amount.csv')

final_failed_tutorials$total = rowSums(final_failed_tutorials[, ])
final_cut_tutorials$total = rowSums(final_cut_tutorials[, ])
final_tutor_amount$total = rowSums(final_tutor_amount[, ])

cols = colnames(final_tutor_amount)
scores = final_failed_tutorials[, cols] + final_tutor_amount[, cols] + final_cut_tutorials[, cols]*0.1

# Por cada franja, y para el total,  obtener la cantidad de tutores optima
for (col in colnames(final_tutor_amount)) {
    df <- data.frame(matrix(ncol = 2, nrow = nrow(final_tutor_amount)))
    x <- c("tutor_amount", "score")
    colnames(df) <- x

    # df$tutor_amount = NA
    df$tutor_amount = final_tutor_amount[, col]
    # df$score = NA
    df$score = scores[, col]

    aggregate(df$score, list(df$tutor_amount), FUN = mean)
   
}