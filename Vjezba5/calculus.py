class calculus:
    @staticmethod
    def numerical_derivative(f, x, epsilon=1e-6, method='three-step'):
        if method == 'three-step':
            return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)
        elif method == 'two-step':
            return (f(x + epsilon) - f(x)) / epsilon
        else:
            raise ValueError("Ne može se derivirati")

    @staticmethod
    def derivative_on_range(f, lower, upper, epsilon=1e-6, method='three-step'):
        points = []
        x_values = [lower + i * epsilon for i in range(int((upper - lower) / epsilon))]
        for x in x_values:
            points.append((x, calculus.numerical_derivative(f, x, epsilon, method)))
        return points
    

    
    
    @staticmethod
    def rectangle_rule(f, lower, upper, num_partitions):
        delta_x = (upper - lower) / num_partitions
        lower_sum = sum(f(lower + i * delta_x) for i in range(num_partitions))
        upper_sum = sum(f(lower + (i + 1) * delta_x) for i in range(num_partitions))
        lower_sum *= delta_x
        upper_sum *= delta_x
        return lower_sum, upper_sum

    @staticmethod
    def trapezoidal_rule(f, lower, upper, num_partitions):
        delta_x = (upper - lower) / num_partitions
        x_values = [lower + i * delta_x for i in range(num_partitions + 1)]
        y_values = [f(x) for x in x_values]
        integral = (sum(y_values) - 0.5 * (y_values[0] + y_values[-1])) * delta_x
        return integral
