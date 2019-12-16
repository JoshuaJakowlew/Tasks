module Main where

solve :: (Int, Int) -> Int
solve (x, y)
    | y <= x    = x^2 + y + 1
    | otherwise = (y + 1)^2 - x

main :: IO ()
main = show . solve . tuplify2 . map read <$> words <$> getLine >>= putStrLn
    where
        tuplify2 [x, y] = (x, y)
