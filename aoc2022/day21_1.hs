import Data.List.Extra
import Functions

data AST
  = Var String Int
  | Add String AST AST
  | Mult String AST AST
  | Div String AST AST
  | Sub String AST AST

main = do
  input <- map parseEither . lines <$> readFile "input/day21.in"
  print input

parse :: [String] -> AST
parse (xs : ": " : ys) = case readMaybe ys of
  Nothing ->
    let ws = words ys
     in case ws of
          [x, "+", y] -> Add xs (Var x 0) (Var y 0)
          [x, "*", y] -> Mult xs (Var x 0) (Var y 0)
          [x, "/", y] -> Div xs (Var x 0) (Var y 0)
          [x, "-", y] -> Sub xs (Var x 0) (Var y 0)
  Just num -> Var xs num
