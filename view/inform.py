class Descriptions:

    # OBJECTIVE FUNCTIONS

    EFFICIENT_RISK = 'Efficient Risk maximizes return for a target risk (semideviation - downside standard deviation). \
                      The resulting portfolio will have a semideviation less than the target (but not guaranteed to be equal).'

    EFFICIENT_RETURN = 'Efficient Return minimizes risk (semideviation - downside standard deviation) for a given target return.'

    MAX_QUADRATIC_UTILITY = 'Maximize Quadratic Utility maximizes the quadratic utility using portfolio semivariance and your chosen \
                            risk aversion parameter.'


    # OPTIMIZERS (MODELS)

    MVO = 'Mean-Variance Optimization derives from the modern portfolio theory (MPT), which was published by Harry Markowitz in 1952 \
        and for which he received the Nobel Prize in Economic Sciences.  The mean-variance-optimization helps the investor to compose a \
        portfolio that has a maximized expected return on a certain level of risk (portfolio variance). When you plot every (multiple) \
        possible combination of your portfolio in a graph with risk (standard deviation) on the x-axis and expected return on the y-axis, \
        the left-boundary of the plotted portfolios create parabola-like shape. The vertex-portfolio will be the closest point to the y-axis. \
        Every portfolio on the left-boundary from the vertex upwards has the highest expected return to a certain risk level thus is pareto efficient.'

    BACKTESTING = "Portfolio backtesting seeks to determine the effectiveness of a trading strategy using historical data. The method takes the \
                portfolio with the selected assets and calculated allocation from the corresponding strategy and compares the performance to the benchmark \
                S&P 500 regarding the given time period."

    # PERFORMANCE INDICATORS

    SHARPE_RATIO = 'The Sharpe ratio is an index for the performance of the portfolio. It is defined as the risk-free return subtracted from the \
    expected return divided by the risk (standard deviation) of the returns.'

descriptions = Descriptions()
    